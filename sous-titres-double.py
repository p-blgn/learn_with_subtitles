# -*- coding: utf-8 -*-
"""
Created on Sat Oct 15 13:25:46 2022

@author: Pierre
"""

import pysrt
import os
import re
import pickle
from pymkv import MKVTrack
import translators as ts

def sub_ger(liste_dir):
    for element in liste_dir:
        if element[-4:] == ".srt" and ("GER" in element):
            return element
def sub_fr(liste_dir):
    for element in liste_dir:
        if element[-4:] == ".srt" and ("FRE" in element):
            return element


L = ["ein", "ist", "der", "bin", "das", "die", "kommst", "komme"]
pickle.dump(L,open("Liste_voca", 'wb'))

liste_dir = os.listdir()
L_subs = []
liste2 = []
L = []
liste_voca = pickle.load(open("Liste_voca",'rb'))
liste_allemand = []
chiffres = ['0','1','2','3','4','5','6','7','8','9']
for ELEMENT in liste_dir:
    if not(os.path.isfile(ELEMENT) or ELEMENT==".git"):
        liste_dir2 = os.listdir(os.getcwd() + "\\" + ELEMENT)
        subs_fr = pysrt.open(os.getcwd() + "\\" + ELEMENT + "\\" + sub_fr(liste_dir2))
        texte = ""
        subs_ger = pysrt.open(os.getcwd() + "\\" + ELEMENT + "\\" + sub_ger(liste_dir2))
        new_subs = pysrt.open(os.getcwd() + "\\" + ELEMENT + "\\" + sub_ger(liste_dir2))
        data_ger = subs_ger.data
        data_fr = subs_fr.data
        new_data = new_subs.data
        for k in range(len(data_ger)):
            element = data_ger[k]
            texte += element.text_without_tags + ' '
            liste_phrases = element.text.split('\n')
            nombre = 0
            for phrase in liste_phrases:
                liste_mots = phrase.split(' ')
                liste_mots2 = []
                for j in range(len(liste_mots)):
                    liste_mots[j] = liste_mots[j].replace('!','').replace('?','').replace(',','').replace(':','').replace(';','')
                    if liste_mots[j] != '' and liste_mots[j][0] == '-':
                        liste_mots[j] = liste_mots[j][1:]
                    a = True
                    for x in liste_mots[j]:
                        if x in chiffres:
                            a = False
                    if not(a):
                        liste_mots2.append(liste_mots[j])
                    if not(liste_mots[j] in liste_voca):
                        nombre += 1
            if nombre >= 2:
                new_data[k].text = data_fr[k].text + '\n' + new_data[k].text
        new_subs.data = new_data
        new_subs.save(os.getcwd() + "\\" + ELEMENT + "\\" + 'test.srt')
"""
Faire attention aux temps, décallage, écart de moins de 400 millisecondes ?
Traduire plutôt que prendre sous-titres français ?
Renommer variables
close
"""