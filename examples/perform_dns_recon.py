import sys,argparse, ipwhois
from redteam import RedTeam
from openpyxl import load_workbook
from ipwhois.net import Net
from ipwhois.asn import IPASN


if len(sys.argv) <= 1:
    print('\n%s -h for help.' % (sys.argv[0]))
    exit(0)

parser = argparse.ArgumentParser()

parser.add_argument("-d",
                    dest="domain",
                    help="domain to enumerate",
                    action='store')

parser.add_argument("-w",
                    dest="wordlist",
                    help="wordlist for forward dns bruteforce",
                    action='store')

args = parser.parse_args()

def get_asn_cidr(ip):

    try:
        net = Net(ip)
        obj = IPASN(net)
        results = obj.lookup()
    except ipwhois.exceptions.IPDefinedError:
        results = {}
        results['asn_cidr'] = 'unknown'
        pass
    return results['asn_cidr']


def main():
    domain = ''
    wordlist_file = ''
    if args.domain:
        domain = args.domain
    x = RedTeam(domain)
    filename_ = x.dnsdumpster()
    wb = load_workbook(filename = "resources/"+filename_)
    sheet_ranges = wb['All Hosts']
    ip_list = []
    asn_cidr_list = []
    for cell in sheet_ranges['B']:
        if 'IP Address' not in cell.value:
            ip_list.append(cell.value)
    ip_list = list(dict.fromkeys(ip_list))
    for ip in ip_list:
        if not get_asn_cidr(ip) == 'unknown':
            asn_cidr_list.append(get_asn_cidr(ip))
    asn_cidr_list = list(dict.fromkeys(asn_cidr_list))
    if args.wordlist:
        wordlist_file = args.wordlist
    x.run_io_tasks_in_parallel([
        lambda: x.dnsaxfr(),
        lambda: x.forward_dns_bruter(domain,wordlist_file),
        lambda: x.reverse_dns_bruter(domain,asn_cidr_list,True)
        ],3)

main()
