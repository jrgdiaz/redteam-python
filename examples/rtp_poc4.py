#proof of concept script to perform forward dns bruteforcing on a base domain

from redteam import RedTeam

wordlist_file = "namelist.txt"
domain = 'example.org'
x = RedTeam(domain)
x.forward_dns_bruter(domain,wordlist_file)
