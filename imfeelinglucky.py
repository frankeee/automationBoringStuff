# -*- coding: utf-8 -*-
"""
Created on Mon Sep 17 01:50:21 2018

@author: Franco

"""

import webbrowser
import  sys
import requests
import bs4

busquedagoogle = "https://www.google.com.ar/search?q="+sys.argv[1]+"&oq="+sys.argv[1]+"&aqs=chrome..69i57j0l5.3144j1j7&sourceid=chrome&ie=UTF-8"

#webbrowser.open(busquedagoogle)

requestgoogle = requests.get(busquedagoogle)
requestgoogle.raise_for_status()
sopitagoogle = bs4.BeautifulSoup(requestgoogle.text)

seleccionagoogle =sopitagoogle.select("h3 a")
i = 0
for r in seleccionagoogle:
    if i > 3:
        break
    else:   
        linkgoogle = seleccionagoogle[i].get("href")
        linkgooglerecortado = linkgoogle[7:(37+len(sys.argv[1]))]
        webbrowser.open(linkgooglerecortado)
        i += 1
