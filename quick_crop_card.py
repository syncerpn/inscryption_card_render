# -*- coding: utf-8 -*-
"""
Created on Sat Apr  9 23:06:14 2022

@author: nghia_sv
"""

from PIL import Image
import numpy as np

ROOT = 'C:/Users/nghia_sv/Desktop/image/'
CARD_PORTRAIT_SOURCE = 'card_portrait/'

img = Image.open(ROOT + CARD_PORTRAIT_SOURCE + 'stoat_character_sheet-resources.assets-3956.png')
img = np.asarray(img.convert('RGBA'))
img = img[:94,:114,:]

Image.fromarray(img).save(ROOT + CARD_PORTRAIT_SOURCE + 'custom_stoat_p03.png')