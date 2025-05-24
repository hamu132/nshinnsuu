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
    #とりあえずデータは2進数にする
    content = ""
    for c in contents:
        content+=nshinsuu.changeN(c,n,2)
    
    print(f"入力データは{n}進数です。")
    print(f"元データ：{contents}\n二進数：{content}\nビット長さ：{len(content)}")
    print()
    


    di = {
        "1":decode.decode,
        "2":decode.decode,
        "10":decode.decode,
        "16":decode.decode
    }


    while True:
        #q = input(">> ")
        if n in di:
            for i in range(3,5):
                bit = 2**i
                #一定ごとに区切る
                contentList = makeList(content,bit)
                decode.decode(contentList,2)
            break
        else:
            print("無効な選択です。")

start()