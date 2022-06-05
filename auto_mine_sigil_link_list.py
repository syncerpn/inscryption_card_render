# -*- coding: utf-8 -*-
"""
Created on Thu Apr  7 01:02:05 2022

@author: nghia_sv
"""

import os
import re

import matplotlib.pyplot as plt
from PIL import Image
import numpy as np

ROOT = 'C:/Users/nghia_sv/Desktop/image/'
file_list = os.listdir(ROOT + 'card_sigil/')
file_list_sigil = [file for file in file_list if file[:7] == 'ability']
sigil_list = dict()

for file in file_list_sigil:
    file_info = re.split('\_|-|\.', file)
    
    sigil = []
    
    is_alternate = False
    for i in range(1,len(file_info)):
        file_type = file_info[i]
        if file_type == 'resources':
            break
        
        if file_type == 'scratched':
            is_alternate = True
            continue
            
        sigil.append(file_type)
    
    sigil = '_'.join(sigil)
    
    if sigil not in sigil_list:
        sigil_list[sigil] = dict()
        sigil_list[sigil]['resources'] = None
        sigil_list[sigil]['alternate'] = None
    
    if is_alternate:
        if not sigil_list[sigil]['alternate']:
            sigil_list[sigil]['alternate'] = file
        else:
            print('[WARN] has 2 alternative:', + file)
    else:
        if not sigil_list[sigil]['resources']:
            sigil_list[sigil]['resources'] = file
        else:
            print('[WARN] has 2 resources:', + file)

with open('sigil_data.txt', 'w') as data_file:
    for sigil in sigil_list:
        line = sigil
        line = line + ',' + sigil_list[sigil]['resources']
        if sigil_list[sigil]['alternate']:
            line = line + ',' + sigil_list[sigil]['alternate']
        else:
            line = line + ','
        line += '\n'
        data_file.write(line)
    
        
i = 1
for sigil in sigil_list:
    sigil_img = Image.open(ROOT + 'card_sigil/' + sigil_list[sigil]['resources'])
    plt.subplot(19,5,i)
    plt.imshow(sigil_img)
    # plt.title(sigil)
    plt.axis('off')
    i=i+1

    # if sigil_list[sigil]['alternate']:
    #     alternate_img = Image.open(ROOT + 'card_sigil/' + sigil_list[sigil]['alternate'])
    #     alternate_img = np.asarray(alternate_img.convert('RGBA'))
    #     alternate_img = alternate_img[:,:,3] > 0
    #     plt.subplots()
    #     plt.imshow(alternate_img)
    #     plt.title(sigil + ' ALTERNATE')
    #     plt.axis('off')