# つくる
# 入力した文字列を punycode に変換し、リポジトリを作成、namecheap の API を叩いて DNS レコードを作成する

from github import Github
import idna
from jinja2 import Environment, FileSystemLoader
import os
import pathlib 
import re

domain = "いんたー.net"

def unicodeToPunycode (unicode: str):
    punycode = idna.encode(unicode)
    return punycode

def punycodeToUnicode (punycode: str):
    unicode = idna.decode(punycode)
    return unicode

def makeDir (path_arg: str, subdomain_unicode: str):
    path = path_arg + '/' + unicodeToPunycode(subdomain_unicode)
    pathlib.Path(path).mkdir(parents=True, exist_ok=True)

def makeHtml (path_arg: str, subdomain: str):
    data = {
        "title" : subdomain + domain,
        "description" : "俺たちの居場所"
    }
    env = Environment(loader = FileSystemLoader('./template'))
    template = env.get_template('001.tpl')
    output_html = open(path_arg + "/" + "index.html", "x")
    output_html.write(template.render(data))

def makeRepo (path_arg: str, subdomain: str):
    return 0

def pushRepo (path):
    # ファイルのアクセスがよくわかっておらず... pathlib がなあ
    github_source = Github(base_url="https://github.com/api/v3", login_or_token=github_token)
    repo = github_source.get_repo(path)
    elements = list()
    for file_path in pathlib.
        element = InputGitTreeElement(file_path, '100644', 'blob', [ファイルの内容] )
        elements.append(element)

    master_ref = repo.get_git_ref("heads/master")
    master_sha = master_ref.object.sha
    base_tree = repo.get_git_tree(master_sha)
    new_tree = repo.create_git_tree(elements, base_tree)
    latest_commit = repo.get_git_commit( master_sha )
    new_commit = repo.create_git_commit("Auto commit by gen-subdomain-repo" ,new_tree, [ latest_commit ] )
    master_ref.edit(new_commit.sha)

path: str = input()
subdomain: str = input()

makeDir(path, subdomain)
