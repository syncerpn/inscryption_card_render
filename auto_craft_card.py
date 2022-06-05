# -*- coding: utf-8 -*-
"""
Created on Fri Apr  8 01:51:45 2022

@author: nghia_sv
"""

import numpy as np
from PIL import Image
import matplotlib.pyplot as plt

from class_Card_data import Card_data as CD
from class_Card_template import select_template

import crafting_helper as crafter
from crafting_helper import Alignment

    
#nghiant: we need some pixel-perfect shit by scaling up every component
#--foil: x4
#--portrait: x4
#--stat_summon: x3
#--font: heavyweight (size, no-scale: 49)
#--stat_power: x3 (size: 147)
#--stat_health: x3 (size: 147)

ROOT = 'C:/Users/nghia_sv/Desktop/image/'
SAVE_DIR = 'collection/'


#tribe
CARD_TRIBE_BIRD = 'card_tribe/tribeicon_bird-resources.assets-3246.png'
CARD_TRIBE_CANINE = 'card_tribe/tribeicon_canine-resources.assets-1637.png'
CARD_TRIBE_HOOVED = 'card_tribe/tribeicon_hooved-resources.assets-1616.png'
CARD_TRIBE_INSECT = 'card_tribe/tribeicon_insect-resources.assets-2422.png'
CARD_TRIBE_REPTILE = 'card_tribe/tribeicon_reptile-resources.assets-2914.png'

card_tribe_ref = {'bird': ROOT + CARD_TRIBE_BIRD, 'canine': ROOT + CARD_TRIBE_CANINE, 'hooved': ROOT + CARD_TRIBE_HOOVED, 'insect': ROOT + CARD_TRIBE_INSECT, 'reptile': ROOT + CARD_TRIBE_REPTILE}
card_tribe_special = ['squirrel']

#portrait
CARD_PORTRAIT_SOURCE = 'card_portrait/'
CARD_OVERLAY_SOURCE = 'card_overlay/'

#sigil dataset
CARD_SIGIL_SOURCE = 'card_sigil/'
with open('sigil_data.csv') as csv_file:
    sigil_data = csv_file.readlines()

sigil_data = [sigil.split(',') for sigil in sigil_data[1:]]
sigil_data_ref = {sigil[0]: ROOT + CARD_SIGIL_SOURCE + sigil[1] for sigil in sigil_data}

#stat
STAT_COST_10BONE = 'card_stat/cost_10bone-resources.assets-3475.png'
STAT_COST_1BLOOD = 'card_stat/cost_1blood-resources.assets-1295.png'
STAT_COST_1BONE = 'card_stat/cost_1bone-resources.assets-1631.png'
STAT_COST_2BLOOD = 'card_stat/cost_2blood-resources.assets-1286.png'
STAT_COST_2BONE = 'card_stat/cost_2bone-resources.assets-3788.png'
STAT_COST_3BLOOD = 'card_stat/cost_3blood-resources.assets-3641.png'
STAT_COST_3BONE = 'card_stat/cost_3bone-resources.assets-4069.png'
STAT_COST_4BLOOD = 'card_stat/cost_4blood-resources.assets-1875.png'
STAT_COST_4BONE = 'card_stat/cost_4bone-resources.assets-3013.png'
STAT_COST_5BONE = 'card_stat/cost_5bone-resources.assets-2576.png'
STAT_COST_6BONE = 'card_stat/cost_6bone-resources.assets-1711.png'
STAT_COST_7BONE = 'card_stat/cost_7bone-resources.assets-2040.png'
STAT_COST_8BONE = 'card_stat/cost_8bone-resources.assets-1279.png'
STAT_COST_9BONE = 'card_stat/cost_9bone-resources.assets-3504.png'
STAT_COST_BLUEGEM = 'card_stat/cost_bluegem-resources.assets-2473.png'
STAT_COST_GREENGEM = 'card_stat/cost_greengem-resources.assets-3959.png'
STAT_COST_ORANGEGEM = 'card_stat/cost_orangegem-resources.assets-4188.png'
STAT_POWER_ANTS = 'card_stat/ants_stat_icon-resources.assets-2013.png'
STAT_POWER_BELL = 'card_stat/bell_stat_icon-resources.assets-1296.png'
STAT_POWER_BONES = 'card_stat/bones_stat_icon-resources.assets-3539.png'
STAT_POWER_CARDSINHAND = 'card_stat/cardsinhand_stat_icon-resources.assets-2081.png'
STAT_POWER_MIRROR = 'card_stat/mirror_stat_icon-resources.assets-3449.png'
STAT_POWER_SACRIFICES = 'card_stat/sacrifices_stat_icon-resources.assets-1957.png'

stat_ref = {'10bone': ROOT + STAT_COST_10BONE,
            '1blood': ROOT + STAT_COST_1BLOOD,
            '1bone': ROOT + STAT_COST_1BONE,
            '2blood': ROOT + STAT_COST_2BLOOD,
            '2bone': ROOT + STAT_COST_2BONE,
            '3blood': ROOT + STAT_COST_3BLOOD,
            '3bone': ROOT + STAT_COST_3BONE,
            '4blood': ROOT + STAT_COST_4BLOOD,
            '4bone': ROOT + STAT_COST_4BONE,
            '5bone': ROOT + STAT_COST_5BONE,
            '6bone': ROOT + STAT_COST_6BONE,
            '7bone': ROOT + STAT_COST_7BONE,
            '8bone': ROOT + STAT_COST_8BONE,
            '9bone': ROOT + STAT_COST_9BONE,
            'bluegem': ROOT + STAT_COST_BLUEGEM,
            'greengem': ROOT + STAT_COST_GREENGEM,
            'orangegem': ROOT + STAT_COST_ORANGEGEM,
            'ants': ROOT + STAT_POWER_ANTS,
            'bell': ROOT + STAT_POWER_BELL,
            'bones': ROOT + STAT_POWER_BONES,
            'cardsinhand': ROOT + STAT_POWER_CARDSINHAND,
            'mirror': ROOT + STAT_POWER_MIRROR,
            'sacrifices': ROOT + STAT_POWER_SACRIFICES}

stat_power_special = ['ants','bell','bones','cardsinhand','mirror','sacrifices']

#name
NAME_SPECIAL_SQUID = 'card_overlay/squid_title-resources.assets-3949.png'
name_special_ref = {'_squid_bell': ROOT + NAME_SPECIAL_SQUID,
                    '_squid_cards': ROOT + NAME_SPECIAL_SQUID,
                    '_squid_mirror': ROOT + NAME_SPECIAL_SQUID}

#card dataset
with open('card_data.csv') as csv_file:
    card_data = csv_file.readlines()
card_data = [crafter.parse_csv_entry(card) for card in card_data[1:]]
            

for card in card_data:
    # if card[CD.KEY] != 'stoat_p03':
    #     continue
    
    if not card[CD.NAME]:
        print('[INFO] skipped unnamed card: "%s"' % card[CD.KEY])
        continue
    
    print('[INFO] crafting: "%s"' % card[CD.KEY])
    #get template
    n_sigil = len(card[CD.SIGIL]) if type(card[CD.SIGIL]) == list else int(card[CD.SIGIL] is not None)
    n_tribe = len(card[CD.TRIBE]) if type(card[CD.TRIBE]) == list else int(card[CD.TRIBE] is not None)
    is_special_stat = True if card[CD.POWER] in stat_power_special else False
    is_with_power = True if card[CD.POWER] else False
    
    template = select_template(foil_type= card[CD.FOIL], n_sigil=n_sigil, is_special_stat=is_special_stat, is_with_power=is_with_power, n_tribe=n_tribe)
    
    #load foil
    card_foil = crafter.prepare_image(ROOT + template.CARD_FOIL, scale=template.SCALE_FOIL)
    
    #load tribe, if any
    tribe_x, tribe_y = template.TRIBE_X, template.TRIBE_Y
    if card[CD.TRIBE]:
        if type(card[CD.TRIBE]) == list:
            assert len(card[CD.TRIBE]) == 5
            card_tribe = []
            for tribe_i in card[CD.TRIBE]:
                card_tribe.append(crafter.prepare_image(card_tribe_ref[tribe_i], scale=template.SCALE_TRIBE))
        elif card[CD.TRIBE] in card_tribe_special:
            card_tribe = None
        else:
            card_tribe = crafter.prepare_image(card_tribe_ref[card[CD.TRIBE]], scale=template.SCALE_TRIBE)
    else:
        card_tribe = None
    
    #load portrait
    portrait_x, portrait_y = template.PORTRAIT_X, template.PORTRAIT_Y
    card_portrait = crafter.prepare_image(ROOT + CARD_PORTRAIT_SOURCE + card[CD.PORTRAIT], scale=template.SCALE_PORTRAIT) if card[CD.PORTRAIT] else None
    
    #load stat:cost
    stat_cost_x, stat_cost_y = template.STAT_COST_X, template.STAT_COST_Y
    card_stat_cost = crafter.prepare_image(stat_ref[card[CD.COST]], scale=template.SCALE_STAT_COST) if card[CD.COST] else None
    
    #power
    stat_power_x, stat_power_y = template.STAT_POWER_X, template.STAT_POWER_Y
    if card[CD.POWER]:
        if is_special_stat:
            card_stat_power = crafter.prepare_image(stat_ref[card[CD.POWER]], scale=template.SCALE_STAT_POWER)
        else:
            card_stat_power = crafter.render_text_object(card[CD.POWER], template.STAT_FONT, template.STAT_FONT_SIZE)
    else:
        card_stat_power = None
    
    #hp
    stat_health_x, stat_health_y = template.STAT_HEALTH_X, template.STAT_HEALTH_Y
    card_stat_hp = crafter.render_text_object(card[CD.HP], template.STAT_FONT, template.STAT_FONT_SIZE) if card[CD.HP] else None
    
    #sigil
    sigil_x, sigil_y = template.SIGIL_X, template.SIGIL_Y
    if card[CD.SIGIL]:
        if type(card[CD.SIGIL]) == list:
            assert len(card[CD.SIGIL]) == 2
            card_sigil = []
            for sigil_i in card[CD.SIGIL]:
                card_sigil.append(crafter.prepare_image(sigil_data_ref[sigil_i], scale=template.SCALE_SIGIL))
        else:
            card_sigil = crafter.prepare_image(sigil_data_ref[card[CD.SIGIL]], scale=template.SCALE_SIGIL)
    else:
        card_sigil = None
    
    #card name
    name_x, name_y = template.NAME_X, template.NAME_Y
    if card[CD.NAME]:
        if card[CD.NAME] in name_special_ref:
            card_name = crafter.prepare_image(name_special_ref[card[CD.NAME]], scale=template.SCALE_NAME)
        else:
            card_name = crafter.render_text_object(card[CD.NAME], template.NAME_FONT, template.NAME_FONT_SIZE, letter_spacing=template.NAME_LETTER_SPACING, max_width=template.NAME_MAX_WIDTH)
    else:
        card_name = None
    
    #overlay
    overlay_x, overlay_y = template.OVERLAY_X, template.OVERLAY_Y
    card_overlay = crafter.prepare_image(ROOT + CARD_OVERLAY_SOURCE + card[CD.OVERLAY], scale=template.SCALE_OVERLAY) if card[CD.OVERLAY] else None
    
    #start crafting
    card_crafted = card_foil.copy()
    if card_tribe is not None:
        if type(card_tribe) == list:
            for card_tribe_i, tribe_x, tribe_y in zip(card_tribe, template.TRIBE_X, template.TRIBE_Y):
                card_crafted = crafter.add_overlay(card_crafted, card_tribe_i, x=tribe_x, y=tribe_y, align=Alignment.TOP_LEFT, overlay_alpha=0.4)
        else:
            card_crafted = crafter.add_overlay(card_crafted, card_tribe, x=tribe_x, y=tribe_y, align=Alignment.TOP_LEFT, overlay_alpha=0.4)
    if card_portrait is not None: card_crafted = crafter.add_overlay(card_crafted, card_portrait, x=portrait_x, y=portrait_y, align=Alignment.TOP_LEFT)
    if card_stat_cost is not None: card_crafted = crafter.add_overlay(card_crafted, card_stat_cost, x=stat_cost_x, y=stat_cost_y, align=Alignment.TOP_RIGHT)
    if card_stat_power is not None: card_crafted = crafter.add_overlay(card_crafted, card_stat_power, x=stat_power_x, y=stat_power_y, align=Alignment.TOP_CENTER)
    if card_stat_hp is not None: card_crafted = crafter.add_overlay(card_crafted, card_stat_hp, x=stat_health_x, y=stat_health_y, align=Alignment.TOP_CENTER)
    if card_sigil is not None:
        if type(card_sigil) == list:
            for card_sigil_i, sigil_x, sigil_y in zip(card_sigil, template.SIGIL_X, template.SIGIL_Y):
                card_crafted = crafter.add_overlay(card_crafted, card_sigil_i, x=sigil_x, y=sigil_y, align=Alignment.MID_CENTER)
        else:
            card_crafted = crafter.add_overlay(card_crafted, card_sigil, x=sigil_x, y=sigil_y, align=Alignment.MID_CENTER)
    if card_name is not None: card_crafted = crafter.add_overlay(card_crafted, card_name, x=name_x, y=name_y, align=Alignment.MID_CENTER)
    if card_overlay is not None: card_crafted = crafter.add_overlay(card_crafted, card_overlay, x=overlay_x, y=overlay_y, align=Alignment.TOP_LEFT)

    Image.fromarray(np.uint8(card_crafted * 255)).save(SAVE_DIR + card[CD.KEY].replace(' ', '_') + '.png')
    # assert 0