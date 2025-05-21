import nshinsuu

def decode(contents,codeType):
    byteList = []
    for c in contents:
        ten = nshinsuu.toTen(c,int(codeType))
        byteList.append(ten)
    try:
        byte = bytes(byteList)
        print(f"{byteList} -> {byte}")
        print("UTF-8を復号します")
        utf8Decode(byte)
    except ValueError:
        print(f"{byteList} -> 変換不可(bit列が不適切です)")
        
    print()

    print("unicodeを復号します")
    for b in byteList:
        uniCodeDecode(b)
    print()

def utf8Decode(byte):
    try:
        print(f"UTF-8 -> {byte.decode('utf-8')} :end")
    except UnicodeDecodeError:
        print("UTF-8は復号できません。")

def uniCodeDecode(byte):
    try:
        print(f"{byte}->{chr(byte)} :end")
    except UnicodeDecodeError:
        print(f"{byte} : Unicodeは復号できません。")
    except ValueError:
        print(f"{byte} : Unicodeは復号できません。")