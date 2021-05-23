import requests
from bs4 import BeautifulSoup
import argparse
import sys
import wget
import csv
import os
import time
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
import ssl
ssl._create_default_https_context = ssl._create_unverified_context


def get_request(url_file, count):
    with open(url_file, 'r', encoding="utf8") as f:
        URLS = f.readlines()

    print('PROGRAM STARTED')
    with open("results.csv", "a") as csv_file:   
        fieldnames = ['Original Site', 'Redirected Site']
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames, delimiter=',')

        writer.writeheader()
    print('CSV FILE CREATED: RESULTS.CSV')

    req_list = []
    URL_LIST = [url.replace('\n','') for url in URLS]
    for url in range(len(URL_LIST)):
        try:
            print("Request to ->", URL_LIST[url])
            r = requests.get(URL_LIST[url], verify=False, timeout=5)
            req_list.append(r)
            if url%count==0 and url/count>=1:
                redirect_lister(req_list)
                req_list = []
                time.sleep(5)
        except:
            pass

def redirect_lister(req_list):
    ORIGINAL_SITES = []
    REDIRECTED_SITES =[]
    for r in req_list:
        history = []
        for site in r.history:
            history.append(site.url)
            if len(history) > 1:
                ORIGINAL_SITES.append(history[0])
                REDIRECTED_SITES.append(history[1])
                print(history[0], " -> ", history[1])
            elif len(history) == 1:
                ORIGINAL_SITES.append(history[0])
                REDIRECTED_SITES.append(r.url)
                print(history[0], " -> ", r.url)



    with open("results.csv", "a") as csv_file:   
        fieldnames = ['Original Site', 'Redirected Site']
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames, delimiter=',')

        for row in range(len(ORIGINAL_SITES)):
            writer.writerow({'Original Site': ORIGINAL_SITES[row], 'Redirected Site': REDIRECTED_SITES[row]})
    
    ORIGINAL_SITES = []
    REDIRECTED_SITES = []

if __name__ == '__main__':
    parser = argparse.ArgumentParser()

    parser.add_argument("-f", "--url_file", required=True, help="Txt file contains target URL's.")
    parser.add_argument("-c", "--count", required=True, help="It defines how many requests has to made before writing to csv.")
    args = vars(parser.parse_args())

    get_request(args['url_file'], int(args['count']))
