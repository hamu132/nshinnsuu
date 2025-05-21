import os
import fileIO
import decode
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


while True:
    path = "data.dat"
    #path = input("暗号ファイルを入力してください（パス）")
    if os.path.isfile(path):
        break
    else:
        print("パスが不正です。")
content = fileIO.openFile(path)

print(content)


di = {
    "1":decode.decode,
    "2":decode.decode
}


print("データの形式を選んでください。")
print("2~16: 2~16進数")
while True:
    #q = input(">> ")
    q = "2"
    if q in di:
        for i in range(2,4):
            bit = 2**i
            contentList = makeList(content,bit)
            print(contentList)
            decode.decode(contentList,q)
        break
    else:
        print("無効な選択です。")

