def changeN(data,fromN,toN):
    if not str(data).isnumeric or not str(fromN).isnumeric or not str(toN).isnumeric:
        return 1
    if int(fromN)<2 or int(toN)<2:
        return 1
    
    temp = toTen(data,fromN)
    result = fromTen(temp,toN)
    return result

def fromTen(data,toN):
    numToStr = {
        0:"0",1:"1",2:"2",3:"3",4:"4",5:"5",6:"6",7:"7",8:"8",9:"9",10:"A",11:"B",12:"C",13:"D",14:"E",15:"F"
    }
    data = int(data)
    result = []
    temp = data
    while True:
        div = temp//toN
        mod = temp%toN
        result = [numToStr[mod]] + result
        temp = div
        if temp==0:
            break
    return "".join(result)

def toTen(data,fromN):
    strToNum = {
        "0":0,"1":1,"2":2,"3":3,"4":4,"5":5,"6":6,"7":7,"8":8,"9":9,"A":10,"B":11,"C":12,"D":13,"E":14,"F":15
    }
    dataList = [strToNum[x] for x in list(data)]
    if max(dataList)>=fromN:
        print("想定しない数が入っているエラー")
        return 0
    result = 0
    for i in range(len(dataList)):
        index = len(dataList)-i-1
        result += dataList[index] * fromN ** i
    return str(result)


def utf8Decode():
    
    print("2進数を入力してください（スペース,改行区切り・qで終了）")
    byte = []
    while True:
        data = input().split(" ")
        if data == ["q"]:
            break
        for i in data:
            for w in list(i):
                if w!="0" and w!="1":
                    print(f"{w}:エラー\n2進数を入力してください")
                    continue
        
        for d in data:
            ten = int(toTen(d,2))
            byte.append(ten)
    return bytes(byte).decode("utf-8")
