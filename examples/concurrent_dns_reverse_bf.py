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
asn_cidr_list = list(dict.fromkeys(asn_cidr_list))
tasks = [lambda ip_Range=ip_Range: x.reverse_dns_bruter(domain,[ip_Range],True) for ip_Range in asn_cidr_list]
print(asn_cidr_list)
x.run_io_tasks_in_parallel(tasks,len(tasks))
