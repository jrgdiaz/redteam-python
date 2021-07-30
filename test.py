from redteam import RedTeam

x = RedTeam('example.org')
subdomains = x.subdomain_recon()

print("=====================reconocimiento de activos en base a certificados digitales publicados en internet========================")

for subdomain in subdomains:
    print(subdomain)

print("=====================dns dumpster dive=====================")

x.dnsdumpster()
