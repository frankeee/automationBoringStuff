# -*- coding: utf-8 -*-
"""
Created on Sun Aug 26 21:53:35 2018

@author: Franco
"""

import random
from random import randint
import os

capitals = {'Alabama': 'Montgomery', 'Alaska': 'Juneau', 'Arizona': 'Phoenix',
   'Arkansas': 'Little Rock', 'California': 'Sacramento', 'Colorado': 'Denver',
   'Connecticut': 'Hartford', 'Delaware': 'Dover', 'Florida': 'Tallahassee',
   'Georgia': 'Atlanta', 'Hawaii': 'Honolulu', 'Idaho': 'Boise', 'Illinois':
   'Springfield', 'Indiana': 'Indianapolis', 'Iowa': 'Des Moines', 'Kansas':
   'Topeka', 'Kentucky': 'Frankfort', 'Louisiana': 'Baton Rouge', 'Maine':
   'Augusta', 'Maryland': 'Annapolis', 'Massachusetts': 'Boston', 'Michigan':
   'Lansing', 'Minnesota': 'Saint Paul', 'Mississippi': 'Jackson', 'Missouri':
   'Jefferson City', 'Montana': 'Helena', 'Nebraska': 'Lincoln', 'Nevada':
   'Carson City', 'New Hampshire': 'Concord', 'New Jersey': 'Trenton',
   'New Mexico': 'Santa Fe', 'New York': 'Albany', 'North Carolina': 'Raleigh',
   'North Dakota': 'Bismarck', 'Ohio': 'Columbus', 'Oklahoma': 'Oklahoma City',
   'Oregon': 'Salem', 'Pennsylvania': 'Harrisburg', 'Rhode Island': 'Providence',
   'South Carolina': 'Columbia', 'South Dakota': 'Pierre', 'Tennessee':
   'Nashville', 'Texas': 'Austin', 'Utah': 'Salt Lake City', 'Vermont':
   'Montpelier', 'Virginia': 'Richmond', 'Washington': 'Olympia',
   'West Virginia': 'Charleston', 'Wisconsin': 'Madison', 'Wyoming': 'Cheyenne'}

quiz = 35

list_capitals = list(capitals.items())

os.makedirs("C:\\Users\\Franco\\Documentos\\Quizes")

for i in range(quiz):
    capitalfile = open("C:\\Users\\Franco\\Documentos\\Quizes\\quiz"+str(i)+".txt","w+")
    capitalfileres = open("C:\\Users\\Franco\\Documentos\\Quizes\\answer"+str(i)+".txt","w+")
    random.shuffle(list_capitals)
    capitalfile.write("Name:\n\nDate:\n\n")
    capitalfileres.write("Answers:\n")
    for r in range(len(list_capitals)):
        estado_city = list_capitals[r]
        capitalfile.write(str(r)+" what is the capital of " + estado_city[0] +"?\n")
        lista_respuestas = []
        lista_respuestas.append(estado_city[1])
        for g in range(3):
            random_capital=random.randint(0,len(list_capitals)-1)
            if (random_capital == r):
                random_capital=random.randint(0,len(list_capitals)-1)
            else:
                sashet = list_capitals[random_capital]
                lista_respuestas.append(sashet[1])
        lista_respuestas.sort()
        for u in range(len(lista_respuestas)):
            capitalfile.write(lista_respuestas[u]+"\n")
        c = 0
        while c<4:
            if estado_city[1] == lista_respuestas[c]:
                break
            else:
                c+=1
        if c == 0:
            capitalfileres.write(str(r)+" .A\n")
        elif c == 1:
            capitalfileres.write(str(r)+" .B\n")
        elif c == 2:
            capitalfileres.write(str(r)+" .C\n")
        elif c == 3:
            capitalfileres.write(str(r)+" .D\n")            
    
            
        