# -*- coding: utf-8 -*-
"""
Created on Tue Feb 11 21:47:02 2020

@author: user
"""
#印出整年度的中獎號碼
import requests
from bs4 import BeautifulSoup
import re
url=('https://www.etax.nat.gov.tw/etw-main/web/ETW183W2_108')

#for i in range(12):
#    if (i%2)!=0:
#        if (i<10):
#            i="0"+str(i)
#        else:
#            i=str(i)
#        rp = requests.get(url+i)
#        rp.encoding='utf-8'
#        soup = BeautifulSoup(rp.text, 'html5lib')
#        all_title=[tag.text.strip()for tag in soup.find_all("td",{"class":"title"})]
#        all_number=[tag.text.strip()for tag in soup.find_all("td",{"class":"number"})]
#        for tit in all_title:
#            print(tit)
#        all_number=str(all_number)
#        all_number=re.findall('[0-9]+',all_number)
#        for num in all_number:
#            print(num)



#輸入月份搜尋
import requests
from bs4 import BeautifulSoup
import re
url=('https://www.etax.nat.gov.tw/etw-main/web/ETW183W2_108')
i=int(input("輸入"+"月份"))
if (i%2)==0:
    i = "0"+str(i-1)
else:
    i = "0"+str(i)
rp = requests.get(url+str(i))
rp.encoding='utf-8'
soup = BeautifulSoup(rp.text, 'html5lib')
all_title=[tag.text.strip()for tag in soup.find_all("td",{"class":"title"})]
all_number=[tag.text.strip()for tag in soup.find_all("td",{"class":"number"})]

for tit in all_title:
   print(tit)
   all_number=str(all_number)
   all_number=re.findall('[0-9]+',all_number)
   for num in all_number:
      print(num)










