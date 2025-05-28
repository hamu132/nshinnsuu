import os
import fileIO
import decode
import nshinsuu
def makeList(content,bit):
    bitList = []
    count = 0
    while True:
        start = count*bit
        end = (count+1)*bit
        if end>len(content):
            break
        bitList.append(content[start:end])
        count+=1
    return bitList


def checkResult(texts,results):
    for r in results:
        count = 0
        if r == None:
            continue

        for w in list(r):
            if w in texts:
                count+=1
        if len(r) == 0:
            print(r)
            return
        rate = count/len(r)
        if rate>0.7:
            print(r)


#0~255
#913~1023
#12288~13311
#-1:そもそも数値にならない
def checkInput(contents):
    numDict = {
        "0":0,"1":1,"2":2,"3":3,"4":4,"5":5,"6":6,"7":7,"8":8,"9":9,
        "A":10,"B":11,"C":12,"D":13,"E":14,"F":15,"G":16,"H":17,"I":18,"J":19,"K":20,"L":21,"M":22,"N":23,"O":24,"P":25,"Q":26,"R":27,"S":28,"T":29,"U":30,"V":31,"W":32,"X":33,"Y":34,"Z":35,
        "a":10,"b":11,"c":12,"d":13,"e":14,"f":15,"g":16,"h":17,"i":18,"j":19,"k":20,"l":21,"m":22,"n":23,"o":24,"p":25,"q":26,"r":27,"s":28,"t":29,"u":30,"v":31,"w":32,"x":33,"y":34,"z":35
    }
    min_n=0
    for c1 in contents:
        for c2 in list(c1):
            if not c2 in numDict.keys():
                return -1
            if min_n<numDict[c2]:
                min_n = numDict[c2]
    return min_n


def start():
    resultsDict = {}
    texts = []
    texts+=(fileIO.openFile("jyouyou.dat"))
    texts+=(fileIO.openFile("words.dat"))

    #スペース等区切りで格納
    contents = fileIO.openFile("data.dat")

    #少なくとも何進数の可能性があるか
    min_n = checkInput(contents)
    if min_n == -1 or min_n>=16:
        print("入力が不適切です。")
        return
    
    #反転か反転しないか
    for inverse in range(2):
        #16からmin_n進数まで
        for n in range(16,min_n,-1):
            #とりあえずデータは2進数にして全部つなげる
            content = ""
            for c in contents:
                content+=nshinsuu.changeN(c,n,2)
            
            # print(f"入力データは{n}進数です。")
            # print(f"元データ：{contents}\n二進数：{content}\nビット長さ：{len(content)}")
            # print()
            #8ビット区切り、16ビット区切りを試す
            for i in range(3,5):
                bit = 2**i
                #一定ごとに区切る
                contentList = makeList(content,bit)
                method = ["utf-8","euc-jp","shift-jis","utf-16-le","utf-16-be"]
                byte = decode.decode(contentList,2,inverse)
                if byte != 0:
                    for m in method:
                        #元進数、区切りビット、手法と結果
                        resultsDict.update(decode.utf8Decode(n,bit,byte,m,inverse))
        print()

    fileIO.writeFile("result.dat",resultsDict)
    checkResult(texts,set(resultsDict.values()))




start()