# -*- coding: utf-8 -*-
"""
Created on Tue Aug 28 15:04:12 2018

@author: Franco
"""

#import webbrowser
import requests
import bs4

#webbrowser.open("https://automatetheboringstuff.com/files")

res = requests.get("https://automatetheboringstuff.com/files/rj.txt")

print(res.status_code==requests.codes.ok)
print(len(res.text))

#print(res.text[:250])

res1 = requests.get('http://inventwithpython.com/page_that_does_not_exist')

try:
    res1.raise_for_status()
except Exception as exc:
    print('There was a problem: ' + str(exc))
    
wachoplay = open("C:\\Users\\Franco\\hello\\wacho.txt","wb")

for chunk in res.iter_content(100000):
    wachoplay.write(chunk)
    
wachoplay.close()

res = requests.get("http://nostarch.com")
res.raise_for_status()
nostarchsoup = bs4.BeautifulSoup(res.text)
type(nostarchsoup)

#weatherfile = open(nostarch.html)
#sopita = bs4.BeautifulSoup(weatherfile)
#type(sopita)


weatherfile = requests.get("https://www.weather.gov")
weatherfile.raise_for_status()
sopitadeclima = bs4.BeautifulSoup(weatherfile.text)
temp = sopitadeclima.select("html body div span")
i = 0
for item in temp:
    print(temp[i].getText())  
    i+=1                         
                        