import argparse

import makeRepo

parser = argparse.ArgumentParser()
parser.add_argument("path", help="specify the path of the directory where the repository will be located")
parser.add_argument("subdomain", help="")
parser.add_argument("--service", choices=["namecheap", "cloudflare"], default="namecheap")

args = parser.parse_args()

unicodeToPunycode()
