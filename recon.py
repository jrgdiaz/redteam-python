# A simple recon module, recon.py
import requests
requests.packages.urllib3.disable_warnings(
requests.packages.urllib3.exceptions.InsecureRequestWarning)
import re
import common_actions
import os
import urllib.parse
from bs4 import BeautifulSoup
from datetime import datetime


"""
OSINT
some of these functions make use of external API's so there are some limits in some cases
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

"""
About the hackertarget api rate limits go to https://hackertarget.com/ip-tools/

50 api calls per day from a single IP

curl -i https://api.hackertarget.com/geoip/?q=1.1.1.1

HTTP/2 200 
server: nginx
date: Wed, 27 Jan 2021 21:17:26 GMT
content-type: text/plain; charset=utf-8
content-length: 91
x-api-quota: 51
x-api-count: 8

IP Address: 1.1.1.1
Country: Australia
Latitude: -33.494
Longitude: 143.2104

"""


"""
checks if axfr possible on domain - using hackertarget api
"""

def dnsaxfr(domain):

    response = requests.get('https://api.hackertarget.com/zonetransfer/?q=%s' % (domain))
    if "XFR size" in response.text:
        print("AXFR possible on %s \n dumping dns records on resources folder..." % (domain))
        now = datetime.now() # current date and time
        date_time = now.strftime("%m%d%Y%H%M%S")
        x = open("resources/dns_axfr_%s_%s.txt" % (domain, date_time),'x')
        x.write(response.text)
        x.close()
    else:
        print("AXFR failed")

def webheaders(domain):
    missing = []
    warnings = []
    results = []
    response = requests.get('https://securityheaders.com/?q=%s&followRedirects=on' % (domain))
    soup = BeautifulSoup(response.text,'lxml')
    report_sections = [report_sections for report_sections in soup.find_all('div',{"class": "reportSection"})]
    for report_section in report_sections:
        report_titles = [report_titles.text.strip() for report_titles in report_section.find_all('div',{"class":"reportTitle"})]
        for report_title in report_titles:
            if report_title == 'Raw Headers':
                print('\nRaw Headers:\n')
                common_actions.scrape_data_from_security_headers(report_section)
            if report_title == 'Missing Headers':
                print('\nMissing Headers:\n')
                missing = common_actions.scrape_data_from_security_headers(report_section,report_title)
            if report_title == 'Warnings':
                print('\nWarnings:\n')
                warnings = common_actions.scrape_data_from_security_headers(report_section,report_title)
    results = missing + warnings
    return results

def urlextract(url):
    headers = requests.utils.default_headers()
    headers.update(
    {
        'User-Agent': 'python',
    }
    )
    response = requests.get('https://urlextractor.net/?target_url=%s&href=1&link_type=all&image=1&meta=1&extract=Extract+Links' % (urllib.parse.quote(url, safe='')),headers=headers)
    soup = BeautifulSoup(response.text,'lxml')
    links = [links['href'] for tbody in soup.find_all('tbody') for trs in tbody.find_all('tr') for tds in trs.find_all('td') for links in tds.find_all('a',href=True)]
    return links

"""
Recon enumeration

"""

def probewebheaders(url):
    headers_items = ''

    try:
        response = requests.get(url,verify=False)
        headers_items = response.headers.items()
        for headers_item in headers_items:
            print(headers_item)
    except:
        print('could not connect to '+url)
    
    return headers_items
