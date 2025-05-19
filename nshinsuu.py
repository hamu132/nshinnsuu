def changeN(data,fromN,toN):
    return

def fromTen(data,toN):
    data = int(data)
    result = []
    temp = data
    while True:
        div = temp//toN
        mod = temp%toN
        result.append(mod)
        temp = div
        if temp==0:
            break
    return "".join()

def toTen(data,fromN):
    dataList = [int(x) for x in list(data)]
    if max(dataList)>=fromN:
        return ValueError
    result = 0
    for i in range(len(dataList)):
        index = len(dataList)-i-1
        result += dataList[index] * fromN ** i
    return result

print(fromTen("123",8))