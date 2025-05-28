from pathlib import Path
import re

#ファイルから暗号データを読み取って配列にする
def openFile(path):
    try:
        with open(Path(path),"r",encoding="utf-8") as file:
            content = file.read()
            returnContent = list(filter(None,re.split(r"[,\s]+",content)))
            return returnContent
    except FileExistsError:
        print("ファイルが存在しません")

#解読ミスを全てファイルに出力
def writeFile(path,contents):
    try:
        with open(Path(path),"w",encoding="utf-8") as file:
            for k,v in contents.items():
                file.write(f"{k} / {v}\n")
    except FileExistsError:
        print("ファイルが存在しません")