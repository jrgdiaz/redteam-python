#proof of concept to find potentially "UI-Redressable" subdomains using OSINT module

from redteam import RedTeam
from datetime import datetime

now = datetime.now() # get current date and time
date_time = now.strftime("%m%d%Y%H%M%S")
domain = 'example.org'
x = RedTeam(domain)
subdomains = x.subdomain_recon()
# store results in a file
file_ = open("resources/clickjacking_%s_%s.txt" % (domain, date_time),'x')
for subdomain in subdomains:
    missing_headers = x.xwebheaders(subdomain)
    if 'X-Frame-Options' in missing_headers:
        print(subdomain+" is vulnerable to clickjacking!")
        file_.write(subdomain+" is vulnerable to clickjacking!\n")   
file_.close()
