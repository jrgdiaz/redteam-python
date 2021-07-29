from redteam import RedTeam

task = RedTeam('example.org')
subdomains = task.subdomain_recon()
for subdomain in subdomains:
    print(subdomain)
