# -*- coding: utf-8 -*-
"""
Created on Mon Jan 31 20:32:06 2022

@author: nghia_sv
"""

#move to 1127, 909
#click one
#move to 1216, 593
#click one
#move to 863, 589
#click one
#move back to 1216, 593
#click one
#repeat whole one


from pynput import mouse, keyboard
import time

mc = mouse.Controller()
kc = keyboard.Controller()

time.sleep(2)

WAIT_SECS = 0.2

for i in range(21):
    mc.position = (1127, 909) #move to ouro
    time.sleep(WAIT_SECS)
    mc.click(mouse.Button.left, 1)
    time.sleep(WAIT_SECS)
    mc.position = (1216, 593) #move to mice
    time.sleep(WAIT_SECS)
    mc.click(mouse.Button.left, 1)
    time.sleep(WAIT_SECS)
    mc.position = ( 863, 589) #move to goat
    time.sleep(WAIT_SECS)
    mc.click(mouse.Button.left, 1)
    time.sleep(WAIT_SECS)
    mc.position = (1216, 593) #move to mice
    time.sleep(WAIT_SECS)
    mc.click(mouse.Button.left, 1)
    time.sleep(WAIT_SECS)
    
    mc.position = (1230, 912) #move to mice 2
    time.sleep(WAIT_SECS)
    mc.click(mouse.Button.left, 1)
    time.sleep(WAIT_SECS)
    mc.position = (1216, 593) #move to ouro
    time.sleep(WAIT_SECS)
    mc.click(mouse.Button.left, 1)
    time.sleep(WAIT_SECS)
    mc.position = ( 863, 589) #move to goat
    time.sleep(WAIT_SECS)
    mc.click(mouse.Button.left, 1)
    time.sleep(WAIT_SECS)
    mc.position = (1216, 593) #move to ouro
    time.sleep(WAIT_SECS+1.5)
    mc.click(mouse.Button.left, 1)
    time.sleep(WAIT_SECS+1)