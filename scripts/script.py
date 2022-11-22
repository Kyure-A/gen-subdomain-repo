import argparse

from . import addDnsRecord
from . import makeRepo

parser = argparse.ArgumentParser()
parser.add_argument("path", help="specify the path of the directory where the repository will be located")
parser.add_argument("subdomain", help="enter the string you would like to use as a subdomain")
parser.add_argument("domain", help="3nter the domain for which you want to create a subdomain", default="")
parser.add_argument("--service", choices=["namecheap", "cloudflare"], default="namecheap" help="")

args = parser.parse_args()

makeRepo.makeRepo(args.path, args.subdomain)
