# redteam-python module
import recon 

class RedTeam:

    domain = ''


    
    def __init__(self, domain):
        self.domain = domain
        print("scope set too: %s" % (self.domain))
    

    def subdomain_recon(self):
        
        print ("performing subdomain recon on %s" % (self.domain))
        subdomains = recon.crt_sh(self.domain)
        return subdomains
    
    def dnsdumpster(self):

        print ("dnsdumpster diving on %s " % (self.domain))
        recon.dnsdumpster(self.domain)
    
    def dnsaxfr(self):
        print("dns axfr on %s" % (self.domain))
        recon.dnsaxfr(self.domain)
  
