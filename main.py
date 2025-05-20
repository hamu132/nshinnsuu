import os
import fileIO
import decode
while True:
    path = "idora.dat"
    #path = input("暗号ファイルを入力してください（パス）")
    if os.path.isfile(path):
        break
    else:
        print("パスが不正です。")
contents = fileIO.openFile(path)


di = {
    "1":decode.decode,
    "2":decode.decode,
    "10":decode.decode,
    "test":decode.nishinnsuukuttuke
}


print("データの形式を選んでください。")
print("2~16: 2~16進数")
while True:
    #q = input(">> ")
    q = "2"
    if q in di:
        di[q](contents,q)
        break
    else:
        print("無効な選択です。")
        break