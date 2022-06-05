# -*- coding: utf-8 -*-
"""
Created on Tue Apr  5 14:49:26 2022

@author: Nghia
"""
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image, ImageDraw, ImageFont
from enum import Enum, auto

#nghiant: from stackoverflow (https://stackoverflow.com/questions/49530282/python-pil-decrease-letter-spacing)

def parse_csv_entry(entry):
    entry = entry.split(',')
    entry_new = []
    i = 0
    flag_list = False
    items = []
    
    while i < len(entry):
        if flag_list:
            item = entry[i]
            if item:
                if item[-1] == '"':
                    flag_list = False
                    items.append(item[:-1])
                    entry_new.append(items)
                else:
                    items.append(item)
            else:
                items.append(item)
            i = i+1
            continue
                
        
        item = entry[i]
        if item:
            if item[0] == '"':
                flag_list = True
                items = [item[1:]]
            else:
                entry_new.append(item)
        else:
            entry_new.append(item)
        i = i+1
        continue
    return entry_new

def draw_text_psd_style(draw, xy, text, font, tracking=0, leading=None, **kwargs):
    """
    usage: draw_text_psd_style(draw, (0, 0), "Test", 
                tracking=-0.1, leading=32, fill="Blue")

    Leading is measured from the baseline of one line of text to the
    baseline of the line above it. Baseline is the invisible line on which most
    letters—that is, those without descenders—sit. The default auto-leading
    option sets the leading at 120% of the type size (for example, 12‑point
    leading for 10‑point type).

    Tracking is measured in 1/1000 em, a unit of measure that is relative to 
    the current type size. In a 6 point font, 1 em equals 6 points; 
    in a 10 point font, 1 em equals 10 points. Tracking
    is strictly proportional to the current type size.
    """
    def stutter_chunk(lst, size, overlap=0, default=None):
        for i in range(0, len(lst), size - overlap):
            r = list(lst[i:i + size])
            while len(r) < size:
                r.append(default)
            yield r
    x, y = xy
    font_size = font.size
    lines = text.splitlines()
    if leading is None:
        leading = font.size * 1.2
    for line in lines:
        for a, b in stutter_chunk(line, 2, 1, ' '):
            w = font.getlength(a + b) - font.getlength(b)
                
            draw.text((x, y), a, font=font, **kwargs)
            x += w + (tracking / 1000) * font_size
        y += leading
        x = xy[0]

#nghiant_end

class Alignment(Enum):
    TOP_LEFT = auto()
    TOP_RIGHT = auto()
    TOP_CENTER = auto()
    MID_LEFT = auto()
    MID_RIGHT = auto()
    MID_CENTER = auto()
    BOT_LEFT = auto()
    BOT_RIGHT = auto()
    BOT_CENTER = auto()

def get_obj_coord(img_ref):
    h, w = img_ref.shape
    
    ys = 0
    ye = h
    xs = 0
    xe = w
    
    while(np.sum(img_ref[ys,:]) == 0):
        ys = ys+1
        
    while(np.sum(img_ref[ye-1,:]) == 0):
        ye = ye-1
        
    while(np.sum(img_ref[:,xs]) == 0):
        xs = xs+1
        
    while(np.sum(img_ref[:,xe-1]) == 0):
        xe = xe-1
    
    return ys,ye,xs,xe

def crop_single_color_object(img, object_color):
    h,w,c = img.shape
    
    channel_list = []
    
    for ic in range(c):
        channel_list.append(img[:,:,ic] == object_color[ic])
    
    object_map = channel_list[0]
    for ic in range(1,c):
        object_map = object_map & channel_list[ic]
    
    ys,ye,xs,xe = get_obj_coord(object_map)
    
    return img[ys:ye, xs:xe, :]

def render_text_object(text, font_name, size, scale=1, color=(0,0,0,255), letter_spacing=None, max_width=None):
    if max_width:
        retry = True
        while retry:
            font = ImageFont.truetype(font_name, size=size)
            retry = False
            render_board = Image.new('RGBA', (1000,1000))
            
            draw = ImageDraw.Draw(render_board)
            if letter_spacing:
                draw_text_psd_style(draw, (10, 10), text, font=font, tracking=letter_spacing, fill=color)
            else:
                draw.text((10, 10), text, font=font, fill=color)
            
            render_board = render_board.resize((int(render_board.size[0] * scale), int(render_board.size[1] * scale)), resample=Image.NEAREST)
            render_board = np.asanyarray(render_board)
            
            text_object = crop_single_color_object(render_board, color)
            text_width = text_object.shape[1]
            if text_width > max_width:
                retry = True
                letter_spacing = letter_spacing * (size-1) / size
                size = size - 1
            
        return np.float32(text_object) / 255
    else:
        font = ImageFont.truetype(font_name, size=size)
        render_board = Image.new('RGBA', (1000,1000))
        
        draw = ImageDraw.Draw(render_board)
        if letter_spacing:
            draw_text_psd_style(draw, (10, 10), text, font=font, tracking=letter_spacing, fill=color)
        else:
            draw.text((10, 10), text, font=font, fill=color)
        
        render_board = render_board.resize((int(render_board.size[0] * scale), int(render_board.size[1] * scale)), resample=Image.NEAREST)
        render_board = np.asanyarray(render_board)
        
        text_object = crop_single_color_object(render_board, color)
        return np.float32(text_object) / 255

def PIL_palette_to_RGBA_numpy_float(img):
    return np.asarray(img.convert('RGBA'), dtype=np.float32) / 255

def prepare_image(img_file, scale=1):
    img = Image.open(img_file)
    img = img.resize((int(img.size[0] * scale), int(img.size[1] * scale)), resample=Image.NEAREST)
    return PIL_palette_to_RGBA_numpy_float(img)

def add_overlay(card_foil, card_portrait, x=0, y=0, align=Alignment.TOP_LEFT, overlay_alpha=1.0):
    ph, pw, pc = card_portrait.shape
    fh, fw, fc = card_foil.shape
    
    assert pc ==  4, '[ERRO] portrait must be RGBA'
    assert pc == fc, '[ERRO] foil must be RGBA'
    
    card_portrait_extended = card_foil * 0
    
    if   align == Alignment.TOP_LEFT:
        card_portrait_extended[y:y+ph, x:x+pw, :] = card_portrait
    elif align == Alignment.TOP_CENTER:
        card_portrait_extended[y:y+ph, x-pw//2:x-pw//2+pw, :] = card_portrait
    elif align == Alignment.TOP_RIGHT:
        card_portrait_extended[y:y+ph, x-pw:x, :] = card_portrait
    elif align == Alignment.MID_CENTER:
        card_portrait_extended[y-ph//2:y-ph//2+ph, x-pw//2:x-pw//2+pw, :] = card_portrait
    
    card_portrait_extended[:,:,3] = card_portrait_extended[:,:,3] * overlay_alpha
    card_crafted = card_foil.copy()
    
    card_crafted[:,:,3:] =  (1.0 - card_portrait_extended[:,:,3:]) * card_foil[:,:,3:] \
                            + card_portrait_extended[:,:,3:]
        
    card_crafted[:,:,:3] = ((1.0 - card_portrait_extended[:,:,3:]) * card_foil[:,:,3:] * card_foil[:,:,:3] \
                            + card_portrait_extended[:,:,3:] * card_portrait_extended[:,:,:3]) / card_crafted[:,:,3:]
    
    return card_crafted