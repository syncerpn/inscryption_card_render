# -*- coding: utf-8 -*-
"""
Created on Wed Apr  6 20:59:02 2022

@author: nghia_sv
"""

import os
import re

import matplotlib.pyplot as plt
from PIL import Image
import numpy as np

ROOT = 'C:/Users/nghia_sv/Desktop/image/'
file_list = os.listdir(ROOT + 'card_portrait/')

file_list_monster = [file for file in file_list if file[:8] == 'portrait']
monster_list = dict()

for file in file_list_monster:
    file_info = re.split('\_|-|\.', file)
    
    monster = []
    
    for i in range(1,len(file_info)):
        file_type = file_info[i]
        if file_type == 'resources' or file_type == 'emission':
            break
        monster.append(file_type)
    
    monster = '_'.join(monster)
    
    if monster not in monster_list:
        monster_list[monster] = dict()
        monster_list[monster]['resources'] = None
        monster_list[monster]['emission'] = None
    
    if file_type in monster_list[monster]:
        if not monster_list[monster][file_type]:
            monster_list[monster][file_type] = file
        else:
            print('[WARN] has alternative: ' + file_type + ' : ' + file)
   
    else:
        print('[INFO] unknown thing: ', file)

with open('portrait_data.txt', 'w') as data_file:
    for monster in monster_list:
        line = monster
        line = line + ',' + monster_list[monster]['resources']
        if monster_list[monster]['emission']:
            line = line + ',' + monster_list[monster]['emission']
        else:
            line = line + ','
        line += '\n'
        data_file.write(line)
        
    
    
# for monster in monster_list:
#     portrait_img = Image.open(ROOT + 'card_portrait/' + monster_list[monster]['resources'])
#     plt.subplots()
#     plt.imshow(portrait_img)
#     plt.title(monster)
#     plt.axis('off')
    
#     if monster_list[monster]['emission']:
#         emission_img = Image.open(ROOT + 'card_portrait/' + monster_list[monster]['emission'])
#         emission_img = np.asarray(emission_img.convert('RGBA'))
#         emission_img = emission_img[:,:,3] > 0
#         plt.subplots()
#         plt.imshow(emission_img)
#         plt.title(monster + ' EMISSION')
#         plt.axis('off')