# -*- coding: utf-8 -*-
"""
Created on Tue Aug 28 15:16:53 2018

@author: Franco
"""

import webbrowser
import sys

direccion = "http://www.google.com/maps/place/"

for r in range(len(sys.argv)-1):
    if r!= 0:
        direccion += "+"+sys.argv[r+1]
    else:
        direccion += sys.argv[r+1]

webbrowser.open(direccion)

