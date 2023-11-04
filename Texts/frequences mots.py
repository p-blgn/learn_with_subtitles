# -*- coding: utf-8 -*-
"""
Created on Mon Oct 31 18:51:13 2022

@author: Pierre
"""

import PyPDF2
import os
from collections import Counter

liste_dir = os.listdir()
LISTE = []
for element in liste_dir:
    if element[-4:] == ".pdf":
        print(element)
        liste = []
        temp = open(element,"rb")
        PDF_read = PyPDF2.PdfFileReader(temp)
        nombre_pages = PDF_read.getNumPages()
        page = ''
        for i in range(nombre_pages):    
            page += PDF_read.getPage(i).extractText()
        n = len(page)
        skip = [";",",",":","!","?","(",")","'",'"',"."]
        split = [" ", '\n']
        texte = ""
        for i in range(n):
            if not(page[i] in skip):
                texte += page[i]
        début = 0
        n = len(texte)
        for i in range(n):
            if texte[i] in split:
                liste.append(texte[début:i])
                début = i+1
        LISTE += liste
l_sorted = Counter(LISTE).most_common()