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
        if os.path.isfile(path):
            break
        else:
            print("パスが不正です。")
    contents = fileIO.openFile(path)
    #とりあえずデータは2進数にする
    content10 = []
    content2 = []
    content16 = []
    for c in contents:
        content10.append(nshinsuu.changeN(c,n,10))
        content2.append(nshinsuu.changeN(c,n,2))
        content16.append(nshinsuu.changeN(c,n,16))
    
    print(f"入力データは{n}進数です。")
    print(f"元データ：{contents}\n二進数：{content2}\n十進数：{content10}\n十六進数：{content16}\nビット長さ：{len("".join(content2))}")
    print()
    



    for i in range(3,5):
        bit = 2**i
        #一定ごとに区切る
        contentList = makeList("".join(content2),bit)
        decode.decode(contentList,2)



start()