import nshinsuu


#2進数に変換して、全部くっつける
def nishinnsuukuttuke(contents,q):
    print(contents)
    byteList = []
    for c in contents:
        two = nshinsuu.changeN(c,10,2)
        byteList.append(two)
    print("".join(byteList))



#10進数に変換して、そのままUTF-8,Unicodeを試す
def decode(contents,codeType):
    byteList = []
    for c in contents:
        ten = nshinsuu.changeN(c,int(codeType),10)
        byteList.append(int(ten))
    try:
        byte = bytes(byteList)
        print(f"10進数：{byteList} -> バイト：{byte}")
        utf8Decode(byte)
    except ValueError:
        print(f"10進数：{byteList}")
        pass
    uniCodeDecode(byteList)




def utf8Decode(byte):
    print("utf-8の解読を試みます...")
    try:
        print(f"utf-8: {byte.decode("utf-8")} end")
    except UnicodeDecodeError:
        print("UTF-8は復号できません。")
    print()

def uniCodeDecode(byteList):
    print("Unicodeの解読を試みます...")
    for b in byteList:
        print(hex(b),end = " ")
    print()
    for b in byteList:
        try:
            print(chr(b),end = ", ")
        except UnicodeDecodeError:
            print("Null",end=", ")
    print()
