from redteam import RedTeam

task = RedTeam('bcie.org')
subdomains = task.subdomain_recon()
for subdomain in subdomains:
    print(subdomain)
