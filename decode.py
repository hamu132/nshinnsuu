import nshinsuu

#バイト型を返す
def decode(contents,codeType,inverse):
    #contentsはビット区切りの二進数配列
    byteList = []
    contents2 = []
    #contentsをコピー、または反転してコピー
    for c in contents:
        contents2.append(nshinsuu.inverse(c,inverse))
    #print(contents,contents2)
    #10進数にしてbyteListに入れる
    for c in contents2:
        ten = nshinsuu.changeN(c,int(codeType),10)
        byteList.append(int(ten))
    try:
        byte = bytes(byteList)
        #print(f"{contents2} -> {byteList} -> {byte}")
        return byte
    except ValueError:
        #print(f"{contents2} -> {byteList} -> 変換不可(bit列が不適切です)")
        return 0




def utf8Decode(n,bit,byte,method,inverse,encode_method):
    try:
        #print(f"{method} -> {byte.decode(method)} :end")
        if inverse == 1:
            inv = "inv"
        else:
            inv = "NOinv"
        return {f"{n}-{bit}-({encode_method}->{method})-{inv}" : byte.decode(method)}
    except UnicodeDecodeError:
        #print(f"{method} -> 復号できません。")
        return {}
    except Exception:
        print("復号できません")
        return {}


def uniCodeDecode(byte):
    try:
        #print(f"{byte}->{chr(byte)} :end")
        return chr(byte)
    except UnicodeDecodeError:
        print(f"{byte} : Unicodeは復号できません。")
    except ValueError:
        print(f"{byte} : Unicodeは復号できません。")
    return ""
    