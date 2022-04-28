import argparse
from redteam import RedTeam

parser = argparse.ArgumentParser()
parser.add_argument("-d", "--domain",
                    dest="domain",
                    help="Check a single Domain.",
                    action='store')
parser.add_argument("-l", "--list",
                    dest="usedlist",
                    help="Check a list of Domains.",
                    action='store')
args = parser.parse_args()
domains = []
if args.domain:
    domains.append(args.domain)
    if args.usedlist:
        with open(args.usedlist, "r",encoding='utf-8') as f:
            for i in f.readlines():
                i = i.strip()
                if i == "" or i.startswith("#"):
                    continue
                domains.append(i)
for domain in domains:
    rt = RedTeam(domain)
    rt.dnsdumpster()
