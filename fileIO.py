from pathlib import Path
import re

#ファイルから暗号データを読み取って配列にする
def openFile(path):
    with open(Path(path),"r",encoding="utf-8") as file:
        content = file.read()
        returnContent = list(filter(None,re.split(r"[,\s]+",content)))
        return returnContent

