from redteam import RedTeam
from openpyxl import load_workbook
from ipwhois.net import Net
from ipwhois.asn import IPASN

def get_asn_cidr(ip):
    net = Net(ip)
    obj = IPASN(net)
    results = obj.lookup()
    return results['asn_cidr']

domain = "example.org"
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
    asn_cidr_list.append(get_asn_cidr(ip))

wordlist_file = "namelist.txt"

x.run_io_tasks_in_parallel([
        lambda: x.dnsaxfr(),
        lambda: x.forward_dns_bruter(domain,wordlist_file),
        lambda: x.reverse_dns_bruter(domain,asn_cidr_list,True)
        ],3)
