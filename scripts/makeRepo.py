# つくる
# 入力した文字列を punycode に変換し、リポジトリを作成、namecheap の API を叩いて DNS レコードを作成する

import idna         # treat punycode
import jinja2
import pathlib
import re

def unicodeToPunycode (unicode: str):
    punycode = idna.encode(unicode)
    return punycode

def punycodeToUnicode (punycode: str):
    unicode = idna.decode(punycode)
    return unicode

def makeDir (path_arg: str, subdomain_unicode: str):
    path = path_arg + "/" + unicodeToPunycode(subdomain_unicode)
    pathlib.Path(path).mkdir()

def makeHtml (path_arg: str):
    return 0

def makeRepo ():
    return 0

makeDir(input(), input())
