#!/usr/bin/env python2

import hal
import os
import time


def turn_on():
    os.system('curl http://shopbot-vacuum.local/cm?cmnd=Power%20On > /dev/null 2> /dev/null')

def turn_off():
    os.system('curl http://shopbot-vacuum.local/cm?cmnd=Power%20Off > /dev/null 2> /dev/null')


h = hal.component("shopbot-vacuum-controller")
h.newpin("on", hal.HAL_BIT, hal.HAL_IN)
h.ready()

old_state = False

try:
    while 1:
        new_state = h['on']
        if new_state and not old_state:
            turn_on()
        elif old_state and not new_state:
            turn_off()
        old_state = new_state
        time.sleep(0.1)

except KeyboardInterrupt:
    pass
