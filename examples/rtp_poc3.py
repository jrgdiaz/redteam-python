#proof of concept script to bruteforce webserver directories massively using recon module

from redteam import RedTeam
from datetime import datetime

wordlist_file = "quickhits.txt"
now = datetime.now() # get current date and time
date_time = now.strftime("%m%d%Y%H%M%S")
domain = 'example.org'
x = RedTeam(domain)
subdomains = x.subdomain_recon()
tasks = [lambda subdomain=subdomain: x.dir_bruter("http://"+subdomain,wordlist_file,wildcard=False) for subdomain in subdomains]
x.run_io_tasks_in_parallel(tasks,len(tasks))
