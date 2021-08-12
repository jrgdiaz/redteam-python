import requests
import os

def download_file(url):
    # Create target Directory if don't exist
    dirName = 'resources'
    if not os.path.exists(dirName):
        os.mkdir(dirName)
        print("Directory " , dirName ,  " Created ")
    else:    
        print("Directory " , dirName ,  " already exists")
    local_filename = url.split('/')[-1]
    # NOTE the stream=True parameter below
    with requests.get(url, stream=True) as r:
        r.raise_for_status()
        with open("resources/"+local_filename, 'wb') as f:
            for chunk in r.iter_content(chunk_size=8192): 
                # If you have chunk encoded response uncomment if
                # and set chunk_size parameter to None.
                #if chunk: 
                f.write(chunk)
    return local_filename

def scrape_data_from_security_headers(report_section,report_title=''):
    return_list = []
    data = [data.text.strip() for tbody in report_section.find_all('tbody') for trs in tbody.find_all('tr') for data in trs.find_all(['th','td'])]
    headers = [data[i] for i in range(len(data)) if i % 2 == 1]
    values = [data[i] for i in range(len(data)) if i % 2 == 0]
    raw = [(values[i],headers[i]) for i in range(0, len(headers))]
    for header in raw:
        print(header)
    if report_title == '' :
        return_list = []
    elif report_title == 'Missing Headers':
        return_list = return_list + values
    elif report_title == 'Warnings':
        return_list = return_list + values
    return return_list
        
        


