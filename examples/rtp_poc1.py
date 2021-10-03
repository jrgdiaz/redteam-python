#proof of concept script to find potentially "UI-Redressable" and unencrypted HTTP subdomains using OSINT module

from redteam import RedTeam
from datetime import datetime

now = datetime.now() # get current date and time
date_time = now.strftime("%m%d%Y%H%M%S")
domain = 'example.org'
x = RedTeam(domain)
subdomains = x.subdomain_recon()
file_ = open("resources\clickjacking_%s_%s.txt" % (domain, date_time),'x')
file2_ = open("resources\http_%s_%s.txt" % (domain,date_time),'x') 
for subdomain in subdomains:
    results = x.xwebheaders(subdomain)
    if 'X-Frame-Options' in results:
        print(subdomain+" is vulnerable to clickjacking!")
        file_.write(subdomain+" is vulnerable to clickjacking!\n")
    if 'Site is using HTTP' in results:   
        print(subdomain+" is using HTTP!")
        file2_.write(subdomain+" is using HTTP!\n")
file_.close()
file2_.close()
