# redteam-python module
import recon 

class RedTeam:

    domain = ''


    
    def __init__(self, domain):
        self.domain = domain
        print("task domain set too: %s" % (self.domain))
    

    #only crt_sh() for now

    def subdomain_recon(self):
        
        print ("performing subdomain recon on %s" % (self.domain))
        subdomains = recon.crt_sh(self.domain)
        return subdomains


