# -*- coding: utf-8 -*-
"""
Created on Sat Apr  9 09:59:33 2022

@author: nghia_sv
"""

def select_template(foil_type='normal', n_sigil=1, is_special_stat=False, is_with_power=False, n_tribe=0):
    if foil_type == 'normal' and n_sigil < 2 and is_special_stat:
        return Card_template_normal_special_stat
    if foil_type == 'normal' and n_sigil == 2:
        return Card_template_normal_double_sigil
    if foil_type == 'rare' and n_sigil == 2 and n_tribe < 2:
        return Card_template_rare_double_sigil
    if foil_type == 'rare' and n_sigil == 1 and n_tribe == 5:
        return Card_template_rare_five_tribe
    if foil_type == 'rare' and n_sigil == 2 and n_tribe == 5:
        return Card_template_rare_double_sigil_five_tribe
    if foil_type == 'rare':
        return Card_template_rare
    if foil_type == 'hare' and is_with_power:
        return Card_template_hare_with_power
    if foil_type == 'hare' and n_sigil == 2:
        return Card_template_hare_double_sigil
    if foil_type == 'hare' and n_sigil < 2:
        return Card_template_hare
    if foil_type == 'normal' and n_sigil < 2 and not is_special_stat:
        return Card_template

class Card_template:
    SCALE_FOIL = 4
    SCALE_TRIBE = 1.7
    SCALE_PORTRAIT = 4
    SCALE_STAT_COST = 3
    SCALE_NAME = 4
    SCALE_SIGIL = 3.6
    SCALE_OVERLAY = 4
    
    TRIBE_X = 0 * SCALE_FOIL
    TRIBE_Y = 0 * SCALE_FOIL
    
    PORTRAIT_X =  6 * SCALE_FOIL
    PORTRAIT_Y = 33 * SCALE_FOIL
    
    STAT_COST_X = 119 * SCALE_FOIL
    STAT_COST_Y =  21 * SCALE_FOIL
    
    STAT_POWER_X =  18 * SCALE_FOIL
    STAT_POWER_Y = 133 * SCALE_FOIL
    
    STAT_HEALTH_X = 107 * SCALE_FOIL
    STAT_HEALTH_Y = 148 * SCALE_FOIL
    
    SIGIL_X =  62 * SCALE_FOIL
    SIGIL_Y = 157 * SCALE_FOIL
    
    NAME_FONT = 'HEAVYWEI.TTF'
    NAME_FONT_SIZE = 24 * SCALE_NAME
    NAME_LETTER_SPACING = 6 * SCALE_NAME
    NAME_MAX_WIDTH = 107 * SCALE_FOIL
    
    NAME_X = 63 * SCALE_FOIL
    NAME_Y = 18 * SCALE_FOIL
    
    STAT_FONT = 'HEAVYWEI.TTF'
    STAT_FONT_SIZE = 49 * SCALE_STAT_COST
    
    CARD_FOIL = 'card_foil/card_empty-resources.assets-3411.png'
    
    OVERLAY_X = 0 * SCALE_OVERLAY
    OVERLAY_Y = 0 * SCALE_OVERLAY

class Card_template_rare(Card_template):
    SCALE_FOIL = Card_template.SCALE_FOIL
    NAME_MAX_WIDTH = 101 * SCALE_FOIL
    CARD_FOIL = 'card_foil/card_empty_rare-resources.assets-1743.png'

class Card_template_hare(Card_template):
    SCALE_FOIL = Card_template.SCALE_FOIL
    NAME_MAX_WIDTH = 101 * SCALE_FOIL
    STAT_HEALTH_X = 95 * SCALE_FOIL
    STAT_HEALTH_Y = 150 * SCALE_FOIL
    CARD_FOIL = 'card_foil/card_terrain_empty-resources.assets-1924.png'
    
class Card_template_normal_double_sigil(Card_template):
    SCALE_FOIL = Card_template.SCALE_FOIL
    STAT_HEALTH_X = 107 * SCALE_FOIL
    STAT_HEALTH_Y = 148 * SCALE_FOIL
    SCALE_SIGIL = 2.6
    SIGIL_X = [ 50 * SCALE_FOIL,  77 * SCALE_FOIL]
    SIGIL_Y = [168 * SCALE_FOIL, 147 * SCALE_FOIL]

class Card_template_normal_special_stat(Card_template):
    SCALE_FOIL = Card_template.SCALE_FOIL
    STAT_POWER_X =  23 * SCALE_FOIL
    STAT_POWER_Y = 130 * SCALE_FOIL
    SCALE_STAT_POWER = 3.6

class Card_template_hare_double_sigil(Card_template_hare):
    SCALE_FOIL = Card_template_hare.SCALE_FOIL
    SCALE_SIGIL = 2.6
    SIGIL_X = [ 35 * SCALE_FOIL,  62 * SCALE_FOIL]
    SIGIL_Y = [168 * SCALE_FOIL, 147 * SCALE_FOIL]
    
class Card_template_rare_double_sigil(Card_template_rare):
    SCALE_FOIL = Card_template_rare.SCALE_FOIL
    SCALE_SIGIL = 2.6
    SIGIL_X = [ 50 * SCALE_FOIL,  77 * SCALE_FOIL]
    SIGIL_Y = [168 * SCALE_FOIL, 147 * SCALE_FOIL]
    
class Card_template_hare_with_power(Card_template_hare):
    SCALE_FOIL = Card_template.SCALE_FOIL
    STAT_HEALTH_X = 107 * SCALE_FOIL
    STAT_HEALTH_Y = 148 * SCALE_FOIL
    
class Card_template_rare_double_sigil_five_tribe(Card_template_rare): #hydra
    SCALE_FOIL = Card_template.SCALE_FOIL
    SCALE_SIGIL = 2.6
    SIGIL_X = [ 35 * SCALE_FOIL,  62 * SCALE_FOIL]
    SIGIL_Y = [168 * SCALE_FOIL, 147 * SCALE_FOIL]
    TRIBE_X = [0 * SCALE_FOIL, 39 * SCALE_FOIL, 78 * SCALE_FOIL, 16 * SCALE_FOIL, 62 * SCALE_FOIL]
    TRIBE_Y = [0 * SCALE_FOIL,  0 * SCALE_FOIL,  0 * SCALE_FOIL, 83 * SCALE_FOIL, 83 * SCALE_FOIL]
    
class Card_template_rare_five_tribe(Card_template_rare): #amalgam
    SCALE_FOIL = Card_template.SCALE_FOIL
    TRIBE_X = [0 * SCALE_FOIL, 39 * SCALE_FOIL, 78 * SCALE_FOIL, 16 * SCALE_FOIL, 62 * SCALE_FOIL]
    TRIBE_Y = [0 * SCALE_FOIL,  0 * SCALE_FOIL,  0 * SCALE_FOIL, 83 * SCALE_FOIL, 83 * SCALE_FOIL]