# -*- coding: utf-8 -*-
"""
Created on Tue Aug 21 15:25:10 2018

@author: Franco
"""

import os
#junta el path con barrras
print(os.path.join("bin","usr","spam"))

files = ["account.txt","sleeper.txt","ragna.txt"]

for filename in files:
    print(os.path.join("c\\users\\franco",filename))
    
#devuelve root path   
print(os.getcwd())
#cambia root path
os.chdir("C:\\Windows\\System32")

print(os.getcwd())

#os.makedirs("C:\\Users\\Franco\\hello.txt")

path = "C:\\Windows32\\System32\\calc.exe"

print(os.path.dirname(path))

print(os.path.basename(path))
#divide en basename y dirname
os.path.split(path)

#devuelve tamaño del archivo
print(os.path.getsize("C:\\Windows\\System32\\calc.exe"))

#muestra archivos que se encuentrane en un directorio
#print(os.listdir("C:"))

#te dice si un path existe o no
print(os.path.exists("C:\\Intel"))

#te dice si el path existe y tiene ese archivo
print(os.path.isfile("C:\\delicious\\walnut\\waffles\\juanca.txt"))

print(os.path.isdir("C:\\Intel"))

#abre archivo
hellofile = open("C:\\Users\\Franco\\hello\\hello.txt")

#lo lee
hello_content = hellofile.read()

print(hello_content)
#printea con espacio 
print(hellofile.readlines())

wachofile = open("C:\\Users\\Franco\\hello\\wacho.txt","w")

wachofile.write("mile \n")
wachofile.write("la mas capa")

wachofile.close()

