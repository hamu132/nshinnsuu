import nshinsuu

def decode(contents,codeType):
    print("反転ナシ")
    decode2(contents,codeType,inverse=False)
    print("反転アリ")
    decode2(contents,codeType,inverse=True)

def decode2(contents,codeType,inverse):
    byteList = []
    for c in contents:
        ten = nshinsuu.changeN(c,int(codeType),10,inverse)
        byteList.append(int(ten))
    try:
        byte = bytes(byteList)
        print(f"{contents} -> {byteList} -> {byte}")
        utf8Decode(byte)
    except ValueError:
        print(f"{contents} -> {byteList} -> 変換不可(bit列が不適切です)")

        
    print()

    unicodeResult = ""
    for b in byteList:
        unicodeResult += uniCodeDecode(b)
    try:
        print(f"UniCode -> {unicodeResult}")
    except:
        print("Unicodeは復号できません。")
    print()

def utf8Decode(byte):
    try:
        print(f"UTF-8 -> {byte.decode('utf-8')} :end")
    except UnicodeDecodeError:
        print("UTF-8 -> 復号できません。")
    try:
        print(f"EUC-JP -> {byte.decode('euc_jp')} :end")
    except UnicodeDecodeError:
        print("EUC-JP -> 復号できません")
    try:
        print(f"SHIFT-JIS -> {byte.decode('shift-jis')} :end")
    except UnicodeDecodeError:
        print("SHIFT-JIS -> 復号できません")
    except Exception:
        print("復号できません")


def uniCodeDecode(byte):
    try:
        #print(f"{byte}->{chr(byte)} :end")
        return chr(byte)
    except UnicodeDecodeError:
        print(f"{byte} : Unicodeは復号できません。")
    except ValueError:
        print(f"{byte} : Unicodeは復号できません。")
    return ""
    