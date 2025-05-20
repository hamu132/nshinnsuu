import nshinsuu

def decode(contents,codeType):
    byteList = []
    for c in contents:
        ten = nshinsuu.toTen(c,int(codeType))
        byteList.append(ten)
    byte = bytes(byteList)
    print(f"{byteList} -> {byte}")
    utf8Decode(byte)
    uniCodeDecode(byte)

def utf8Decode(byte):
    try:
        print(byte.decode("utf-8"))
    except UnicodeDecodeError:
        print("UTF-8は復号できません。")

def uniCodeDecode(byte):
    try:
        print(chr(byte))
    except UnicodeDecodeError:
        print("Unicodeは復号できません。")