def changeN(data,fromN,toN):
    return

def fromTen(data,toN):
    return

def toTen(data,fromN):
    dataList = [int(x) for x in list(data)]
    if max(dataList)>=fromN:
        return ValueError
    result = 0
    for i in range(len(dataList)):
        index = len(dataList)-i-1
        result += dataList[index] * fromN ** i
    return result

print(toTen("1010",2))