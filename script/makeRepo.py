# つくる
# 入力した文字列を punycode に変換し、リポジトリを作成、namecheap の API を叩いて DNS レコードを作成する

import idna         # treat punycode
import namecheap
import pathlib
import re

api = namecheap.Api(username, api_key, username, ip_address, sandbox = True)

def unicodeToPunycode (unicode: str):
    punycode = idna.encode(unicode)
    return punycode

def punycodeToUnicode (punycode: str):
    unicode = idna.decode(punycode)
    return unicode

def makedir (path_arg, subdomain_unicode):
    path = path_arg + "/" + unicodeToPunycode(subdomain_unicode)
    pathlib.Path(path).mkdir()


