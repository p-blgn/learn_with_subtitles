 # -*- coding: utf-8 -*-
"""
Created on Tue Oct 11 18:59:59 2022

@author: Pierre
"""

import pysrt
import os
import re
from googletrans import Translator
import json
import pickle

liste_dir = os.listdir()
voca = pickle.load(open("Liste_voca_de", 'rb'))
texte = ""
L_subs = []
liste2 = []
L = []
f = open('german-english.json')
dico = json.load(f)
chiffres = ['0','1','2','3','4','5','6','7','8','9']
for element in liste_dir:
    if element[-4:] == ".srt":
        L_subs.append(open(element,'rb'))
        subs = pysrt.open(element)
        data = subs.data
        for element in data:
            texte += element.text + '\n'
texte = texte.replace('.','').replace("<i>",'').replace("</i>",'').replace(',','').replace(';','').replace('"','').replace(':','').replace('?','').replace('!','')
liste = re.split(' |\n', texte)
for i in range(len(liste)):
    if liste[i] != '' and liste[i][0] == '-':
        liste[i] = liste[i].replace("-","")
for element in liste:
    a = True
    for x in element:
        if x in chiffres:
            a = False
    if len(element)>2 and a:
        liste2.append(element)
liste2.sort()
liste = [liste2[0]]
occurences = [1]
for i in range(1,len(liste2)):
    if liste2[i-1] == liste2[i]:
        occurences[-1] += 1
    else:
        occurences.append(1)
        liste.append(liste2[i])
inconnus = []
for mot in liste:
    if not(mot in voca):
        inconnus.append(mot)