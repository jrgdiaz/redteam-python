# A simple recon module, recon.py
import requests
import re
import common_actions
import os
from bs4 import BeautifulSoup


"""
OSINT

"""

"""
fetches data from crt_sh for URL
"""
def crt_sh(domain):
    x = []
    print("Fetching data from crt.sh")
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

"""
fetches data from dnsdumpster for URL
"""
def dnsdumpster(domain):
    
    
    r = requests.get('https://dnsdumpster.com/')
    csrftoken = r.cookies['csrftoken']
    
    s = BeautifulSoup(r.text,'lxml')
    csrf_token=s.find("input",{"name":"csrfmiddlewaretoken"})['value']
    cookies = {'csrftoken':csrf_token}
    referer = {'Referer':'https://dnsdumpster.com'}
    data = {'csrfmiddlewaretoken':csrf_token,'targetip':domain,'user':'free'}
    response = requests.post('https://dnsdumpster.com/', data=data, cookies=cookies,headers=referer)
    soup = BeautifulSoup(response.text,'lxml')
    info = [a['href'] for a in soup.find_all('a', href=True)]
    for i in info:
        if 'xls' in i or 'graph' in i:
            local_filename = common_actions.download_file('https://dnsdumpster.com/%s' % (i))
            if 'html' in local_filename:
                #we have to edit the dnsdumpster html file in order to view the graph.
                f = open("resources/"+local_filename, "r")
                s = re.sub('/static/','https://dnsdumpster.com/static/',f.read())
                x = open("resources/new_"+local_filename, "w")
                x.write(s)
                f.close()
                os.remove("resources/"+local_filename)
                x.close()
