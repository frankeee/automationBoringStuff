# -*- coding: utf-8 -*-
"""
Created on Tue Sep 18 02:25:30 2018

@author: Franco
"""

import requests
import bs4
import os
import sys

cant = sys.argv[1]
rome = int(cant)
os.makedirs("C:\\Users\\Franco\\Documents\\xkcdcomics")
i = 1
while i<rome:   
    xkcd = "https://xkcd.com/"+str(i)+"/"
    requestxkcd = requests.get(xkcd)
    requestxkcd.raise_for_status()
    sopaxk =bs4.BeautifulSoup(requestxkcd.text)
    
    linkxkc = sopaxk.select("#comic img")
    img1xkcd = linkxkc[0].get("src")
    imgxkcd = "http:"+img1xkcd 
    
    print(imgxkcd)
    
    requestdefi = requests.get(imgxkcd)
    requestdefi.raise_for_status()
    
    xkcdfile = open("C:\\Users\\Franco\\Documents\\xkcdcomics\\xkcd"+str(i)+".png","wb+")
    
    for binarios in requestdefi.iter_content(1000):
        xkcdfile.write(binarios)
    i += 1
