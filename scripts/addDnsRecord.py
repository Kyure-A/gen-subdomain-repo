import namecheap

from . import makeRepo

# required credential.py
api = namecheap.Api(username, api_key, username, ip_address, sandbox = True)

def makeDnsRecord (subdomain: str):
    record = [
        {
            "Type": "A",
            "Name": subdomain,
            "Address": "185.199.108.153",
            "TTL": "1800"
        },

        {
            "Type": "A",
            "Name": subdomain,
            "Address": "185.199.109.153",
            "TTL": "1800"
        },

        {
            "Type": "A",
            "Name": subdomain,
            "Address": "185.199.110.153",
            "TTL": "1800"
        },       

        {
            "Type": "A",
            "Name": subdomain,
            "Address": "185.199.111.153",
            "TTL": "1800"
        }
    ]

    return record

def addDnsRecord (domain: str, subdomain: str):
    for record in makeDnsRecord(subdomain):
        api.domains_dns_addHost(domain, record)

def delDnsRecord (domain: str, subdomain: str):
    # 工事中
    record = makeDnsRecord(subdomain)
    return record
