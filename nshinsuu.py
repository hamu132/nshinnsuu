def changeN(data,fromN,toN):
    temp = toTen(data,fromN)
    result = fromTen(temp,toN)
    return result

def fromTen(data,toN):
    data = int(data)
    result = []
    temp = data
    while True:
        div = temp//toN
        mod = temp%toN
        result = [str(mod)] + result
        temp = div
        if temp==0:
            break
    two = "".join(result)

    li = [4,8,16]
    count = 0
    for i in li:
        count = i - len(two)
        if count>=0:
            break
    return "0"*count + two

def toTen(data,fromN):
    dataList = [int(x) for x in list(data)]
    if max(dataList)>=int(fromN):
        print("エラー")
        return 0
    result = 0
    for i in range(len(dataList)):
        index = len(dataList)-i-1
        result += dataList[index] * int(fromN) ** i
    return result


#print(changeN("10",10,2))