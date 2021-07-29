from redteam import RedTeam

engagement = RedTeam('example.org')
subdomains = engagement.subdomain_recon()
for subdomain in subdomains:
    print(subdomain)
