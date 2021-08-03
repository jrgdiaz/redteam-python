from redteam import RedTeam

x = RedTeam('github.com')
subdomains = x.subdomain_recon()

print("=====================reconocimiento de activos en base a certificados digitales publicados en internet========================")

for subdomain in subdomains:
    print(subdomain)

print("=====================dns dumpster dive=====================")

x.dnsdumpster()

print("=====================dns axfr test=====================")

x.dnsaxfr()
