def changeN(data,fromN,toN,inverse):
    if inverse:
        inverseData = ""
        for d in list(data):
            if d == "1":
                inverseData+="0"
            else:
                inverseData+="1"
        data = inverseData
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
    numDict = {
        "0":0,"1":1,"2":2,"3":3,"4":4,"5":5,"6":6,"7":7,"8":8,"9":9,
        "A":10,"B":11,"C":12,"D":13,"E":14,"F":15,
        "a":10,"b":11,"c":12,"d":13,"e":14,"f":15
    }
    dataList = [numDict[x] for x in list(data)]
    if max(dataList)>=int(fromN):
        print("エラー")
        return 0
    result = 0
    for i in range(len(dataList)):
        index = len(dataList)-i-1
        result += dataList[index] * int(fromN) ** i
    return result


#print(changeN("10",10,2))