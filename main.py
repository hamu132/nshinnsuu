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

def start():
    while True:
        path = "data.dat"
        n = "10"
        #path = input("暗号ファイルを入力してください（パス）")
        if os.path.isfile(path):
            break
        else:
            print("パスが不正です。")
    contents = fileIO.openFile(path)
    print(contents,len(contents))
    #とりあえずデータは2進数にするa
    content = ""
    for c in contents:
        content+=nshinsuu.changeN(c,n,2)
    print(content,len(content))
    


    di = {
        "1":decode.decode,
        "2":decode.decode,
        "10":decode.decode
    }


    print(f"入力データは{n}進数です。")
    while True:
        #q = input(">> ")
        if n in di:
            for i in range(2,5):
                bit = 2**i
                #一定ごとに区切る
                contentList = makeList(content,bit)
                print(contentList)
                decode.decode(contentList,2)
            break
        else:
            print("無効な選択です。")

start()