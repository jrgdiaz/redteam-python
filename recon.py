# A simple recon module, recon.py
import requests
import re
from bs4 import BeautifulSoup




"""
fetches data from crt_sh for URL
"""
def crt_sh(domain):
    x = []
    response = requests.get('https://crt.sh/?q=%s' % (domain))
    s = re.sub('<BR>',' ',response.text)
    soup = BeautifulSoup(s,'lxml')
    subdomains = [tr.find_all('td')[5].text.strip() for tr in soup.find_all('tr')[6:]]
    #the following can probably be improved using more list comprehension
    for subdomain in subdomains:
        if ' ' in subdomain:
            for i in subdomain.split(' '):
                x.append(i)
        else:
            x.append(subdomain)
    x = list(dict.fromkeys(x))

    return x
    

    
        