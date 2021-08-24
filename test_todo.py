from redteam import RedTeam
import workspace
from datetime import datetime
wordlist_file = "C:\\Users\\GS65\\Desktop\\redteam-python-main\\quickhits.txt"
now = datetime.now() # get current date and time
date_time = now.strftime("%m%d%Y%H%M%S")
domain = 'pucmm.edu.do'
x = RedTeam(domain)
subdomains = x.subdomain_recon()
tasks = [lambda subdomain=subdomain: x.dir_bruter("http://"+subdomain,wordlist_file) for subdomain in subdomains]
workspace.run_io_tasks_in_parallel(tasks)
