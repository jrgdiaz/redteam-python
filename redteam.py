# redteam-python module
import recon
import common_actions

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




