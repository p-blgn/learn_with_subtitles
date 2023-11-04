# -*- coding: utf-8 -*-
"""
Created on Sat Oct 29 14:11:57 2022

@author: Pierre
"""

import PyPDF2
temp = open('C:/Users/pierr/Documents/Python Scripts/Sous-titres/Dictionnaire Français-Allemand.pdf', 'rb')
PDF_read = PyPDF2.PdfFileReader(temp)
nombre_pages = PDF_read.getNumPages()
page = ''
for i in range(nombre_pages):    
    page += PDF_read.getPage(i).extractText()
liste = page.split('\n')
liste = liste[3:]