# -*- coding: utf-8 -*-
"""
Created on Tue Apr  5 00:47:12 2022

@author: nghia_sv
"""

import numpy as np
from PIL import Image
import matplotlib.pyplot as plt
import crafting_helper as crafter
from crafting_helper import Alignment

#nghiant: we need some pixel-perfect shit by scaling up every component
#--foil: x4
#--portrait: x4
#--stat_summon: x3
#--font: heavyweight (size, no-scale: 49)
#--stat_power: x3 (size: 147)
#--stat_health: x3 (size: 147)

SCALE_FOIL = 4
SCALE_TRIBE = 1.7
SCALE_PORTRAIT = 4
SCALE_STAT_SUMMON = 3
SCALE_NAME = 4
SCALE_SIGIL = 3.6

TRIBE_X = 0
TRIBE_Y = 0

PORTRAIT_X =  6 * SCALE_FOIL
PORTRAIT_Y = 33 * SCALE_FOIL

STAT_SUMMON_X = 119 * SCALE_FOIL
STAT_SUMMON_Y =  21 * SCALE_FOIL

STAT_POWER_X =  18 * SCALE_FOIL
STAT_POWER_Y = 133 * SCALE_FOIL

STAT_HEALTH_X = 107 * SCALE_FOIL
STAT_HEALTH_Y = 148 * SCALE_FOIL

SIGIL_X =  62 * SCALE_FOIL
SIGIL_Y = 157 * SCALE_FOIL

NAME_FONT = 'HEAVYWEI.TTF'
NAME_FONT_SIZE = 24 * SCALE_NAME
NAME_LETTER_SPACING = 6 * SCALE_NAME

NAME_X = 63 * SCALE_FOIL
NAME_Y =  8 * SCALE_FOIL

STAT_FONT = 'HEAVYWEI.TTF'
STAT_FONT_SIZE = 49 * SCALE_STAT_SUMMON

ROOT = 'C:/Users/nghia_sv/Desktop/image/'
# ROOT = './'
CARD_FOIL_SOURCE = 'card_foil/card_empty-resources.assets-3411.png'
CARD_TRIBE_SOURCE = 'card_tribe/tribeicon_hooved-resources.assets-1616.png'
CARD_PORTRAIT_SOURCE = 'card_portrait/portrait_goat-resources.assets-3441.png'
CARD_STAT_SUMMON_SOURCE = 'card_stat/cost_1blood-resources.assets-1295.png'
CARD_STAT_POWER = 0
CARD_STAT_HEALTH = 1
CARD_SIGIL_SOURCE = 'card_sigil/ability_tripleblood-resources.assets-3968.png'
CARD_NAME = 'black goat'


# CARD_PORTRAIT_SOURCE = 'card_portrait/portrait_direwolf-resources.assets-1518.png'
# CARD_TRIBE_SOURCE = 'card_tribe/tribeicon_canine-resources.assets-1637.png'
# CARD_STAT_SUMMON_SOURCE = 'card_stat/cost_3blood-resources.assets-3641.png'
# CARD_STAT_POWER = 2
# CARD_STAT_HEALTH = 5
# CARD_SIGIL_SOURCE = 'card_sigil/ability_doublestrike-resources.assets-1952.png'
# CARD_NAME = 'dire wolf'


# CARD_PORTRAIT_SOURCE = 'card_portrait/portrait_wolf-resources.assets-3815.png'
# CARD_TRIBE_SOURCE = 'card_tribe/tribeicon_canine-resources.assets-1637.png'
# CARD_STAT_SUMMON_SOURCE = 'card_stat/cost_2blood-resources.assets-1286.png'
# CARD_STAT_POWER = 3
# CARD_STAT_HEALTH = 2
# CARD_SIGIL_SOURCE = 'card_sigil/ability_doublestrike-resources.assets-1952.png'
# CARD_NAME = 'wolf'


CARD_PORTRAIT_SOURCE = 'card_portrait/portrait_ravenegg-resources.assets-1855.png'
CARD_TRIBE_SOURCE = 'card_tribe/tribeicon_bird-resources.assets-3246.png'
CARD_STAT_SUMMON_SOURCE = 'card_stat/cost_1blood-resources.assets-1295.png'
CARD_STAT_POWER = 0
CARD_STAT_HEALTH = 2
CARD_SIGIL_SOURCE = 'card_sigil/ability_evolve_1-resources.assets-2713.png'
CARD_NAME = 'raven egg'


# CARD_PORTRAIT_SOURCE = 'card_portrait/portrait_adder-resources.assets-3623.png'
# CARD_TRIBE_SOURCE = 'card_tribe/tribeicon_reptile-resources.assets-2914.png'
# CARD_STAT_SUMMON_SOURCE = 'card_stat/cost_2blood-resources.assets-1286.png'
# CARD_STAT_POWER = 1
# CARD_STAT_HEALTH = 1
# CARD_SIGIL_SOURCE = 'card_sigil/ability_deathtouch-resources.assets-3909.png'
# CARD_NAME = 'adder'

# CARD_TRIBE_SOURCE = 'card_tribe/tribeicon_bird-resources.assets-3246.png'

card_foil = crafter.prepare_image(ROOT + CARD_FOIL_SOURCE, scale=SCALE_FOIL)
card_tribe = crafter.prepare_image(ROOT + CARD_TRIBE_SOURCE, scale=SCALE_TRIBE)
card_portrait = crafter.prepare_image(ROOT + CARD_PORTRAIT_SOURCE, scale=SCALE_PORTRAIT)
card_stat_summon = crafter.prepare_image(ROOT + CARD_STAT_SUMMON_SOURCE, scale=SCALE_STAT_SUMMON)
stat_power = crafter.render_text_object(str(CARD_STAT_POWER), STAT_FONT, STAT_FONT_SIZE)
stat_health = crafter.render_text_object(str(CARD_STAT_HEALTH), STAT_FONT, STAT_FONT_SIZE)
card_sigil = crafter.prepare_image(ROOT + CARD_SIGIL_SOURCE, scale=SCALE_SIGIL)
card_name = crafter.render_text_object(str(CARD_NAME), NAME_FONT, NAME_FONT_SIZE, letter_spacing=NAME_LETTER_SPACING)

#crafting
card_crafted = crafter.add_overlay(card_foil, card_tribe, x=TRIBE_X, y=TRIBE_Y, align=Alignment.TOP_LEFT, overlay_alpha=0.4)
card_crafted = crafter.add_overlay(card_crafted, card_portrait, x=PORTRAIT_X, y=PORTRAIT_Y, align=Alignment.TOP_LEFT)
card_crafted = crafter.add_overlay(card_crafted, card_stat_summon, x=STAT_SUMMON_X, y=STAT_SUMMON_Y, align=Alignment.TOP_RIGHT)
card_crafted = crafter.add_overlay(card_crafted, stat_power, x=STAT_POWER_X, y=STAT_POWER_Y, align=Alignment.TOP_CENTER)
card_crafted = crafter.add_overlay(card_crafted, stat_health, x=STAT_HEALTH_X, y=STAT_HEALTH_Y, align=Alignment.TOP_CENTER)
card_crafted = crafter.add_overlay(card_crafted, card_sigil, x=SIGIL_X, y=SIGIL_Y, align=Alignment.MID_CENTER)
card_crafted = crafter.add_overlay(card_crafted, card_name, x=NAME_X, y=NAME_Y, align=Alignment.TOP_CENTER)

# plt.subplots()
# plt.imshow(stat_power)

plt.subplots()
plt.imshow(card_crafted)
Image.fromarray(np.uint8(card_crafted * 255)).save(CARD_NAME.replace(' ', '_') + '.png')
