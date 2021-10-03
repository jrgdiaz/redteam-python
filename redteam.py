# redteam-python module
import recon
import common_actions
from metagoofil import Metagoofil
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

    def getLinks(self,x):
        print("extracting urls from %s" %(x))
        links = recon.getLinks(x)
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
    def metagoofil(self,
        x=None,
        delay=30.0,
        save_links=False,
        url_timeout=15,
        search_max=100,
        download_file_limit=100,
        save_directory="resources/",
        number_of_threads=8,
        file_types=['pdf','doc','xls','ppt','odp','ods','docx','xlsx','pptx'],
        user_agent='Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)',
        download_files=False,
    
    ):
        if x is None:
            mg = Metagoofil(self.domain,
            delay,
            save_links,
            url_timeout,
            search_max,
            download_file_limit,
            save_directory,
            number_of_threads,
            file_types,
            user_agent,
            download_files,
            )
            mg.go()
            print("[+] Done!")
        else:
            mg = Metagoofil(
            x,
            delay,
            save_links,
            url_timeout,
            search_max,
            download_file_limit,
            save_directory,
            number_of_threads,
            file_types,
            user_agent,
            download_files,
            )
            mg.go()
            print("[+] Done!")

    def googledork(self,query):
        hits = recon.googledork(query)
        return hits
