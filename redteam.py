# redteam-python module
import recon
import common_actions
from concurrent.futures import ThreadPoolExecutor


class RedTeam:

    domain = ''
    
    def __init__(self, domain=None):
        self.domain = domain
        print("scope set too: %s" % (self.domain))

    def subdomain_recon(self):
        
        print ("performing subdomain recon on %s" % (self.domain))
        subdomains = recon.crt_sh(self.domain)
        return subdomains
    
    def dnsdumpster(self,x=None):
        print ("dnsdumpster diving on %s " % (self.domain))
        recon.dnsdumpster(self.domain)
    
    def dnsaxfr(self):
        print("dns axfr on %s" % (self.domain))
        recon.dnsaxfr(self.domain)

    def xwebheaders(self,x=None):
        if x is None:
            print("webserver headers on %s" % (self.domain))
            missing_headers = recon.webheaders(self.domain)
        else:
            print("webserver headers on %s" % (x+"/"))
            missing_headers = recon.webheaders(x+"/")
        return missing_headers

    def probewebheaders(self,x):
        print("webserver headers on %s" % (x))
        headers = recon.probewebheaders(x)
        return headers

    def urlextract(self,x):
        print("extracting urls from %s" % (x))
        links = recon.urlextract(x)
        return links
    
    def dir_bruter(self,x,wordlist_file,extensions=None,wildcard=True):
        print("directory bruteforcing on %s" %(x))
        word_queue = common_actions.build_wordlist(wordlist_file)
        recon.dir_bruter(x,word_queue,extensions,wildcard)
    
    def run_io_tasks_in_parallel(self,tasks,max_workers):
        with ThreadPoolExecutor(max_workers=max_workers) as executor: 
            running_tasks = [executor.submit(task) for task in tasks]
            for running_task in running_tasks:
                running_task.result()

    """
        run_io_tasks_in_parallel([
        lambda: print('IO task 1 running!'),
        lambda: print('IO task 2 running!'),
        ])
"""
