# -------------------------------------------------------------------------------------------
# File : neopixel_ring.py
# Desc : This file contains functions to control the neopixel ring
# -------------------------------------------------------------------------------------------

import array, time
from machine import Pin
from color_map import *
import rp2

#region: GLOBAL CONSTANTS AND VARIABLES -----------------------------------------------------

# ===== VARIABLES ===========================================================================
NUM_LEDS = 16                                   # Number of neopixels in the ring
PIN_NUM = 1                                     # Pin where the neopixel ring is connected
brightness = 0.02                               # from 0 to 1 -> take care, 1 is very bright!

#endregion ----------------------------------------------------------------------------------


#region: FUNCTIONS DEFINITION ---------------------------------------------------------------

# ===== FUNCTIONS FOR PIO ===================================================================
# FUNCTION: PIO assembly code to drive the WS2812 LEDs
@rp2.asm_pio(sideset_init=rp2.PIO.OUT_LOW, out_shiftdir=rp2.PIO.SHIFT_LEFT, autopull=True, pull_thresh=24)  # CHANGE: line length
def ws2812():
    T1 = 2
    T2 = 5
    T3 = 3
    wrap_target()
    label("bitloop")
    out(x, 1)               .side(0)    [T3 - 1]
    jmp(not_x, "do_zero")   .side(1)    [T1 - 1]
    jmp("bitloop")          .side(1)    [T2 - 1]
    label("do_zero")
    nop()                   .side(0)    [T2 - 1]
    wrap()

# Create the StateMachine with the ws2812 program, outputting on Pin(PIN_NUM).
sm = rp2.StateMachine(0, ws2812, freq=8_000_000, sideset_base=Pin(PIN_NUM))

# Start the StateMachine, it will wait for data on its FIFO.
sm.active(1)

# ===== FUNCTIONS FOR NEOPIXEL RING OPERATION =============================================
# FUNCTION: Create the 24 bit data for each neopixel in the GRB order with desired brightness
def pixel_set_and_dim(color, brightness):
    green=int(color[1]*brightness)
    red=int(color[0]*brightness)
    blue=int(color[2]*brightness)
    result= (green<<16)+(red<<8)+blue
    return result

# FUNCTION: Create an array with the 24 bits value of GRB for all pixels and sends it to the PIO
def draw_ring(ring,num_leds):
    # Creates an array, type of elements: unsigned integer,
    # initialized with a zeroed list of num_leds size
    # Array type, see : https://docs.python.org/3/library/array.html
    ar = array.array("I",[0]*num_leds)
    for i, color in enumerate(ring):
        ar[i]=pixel_set_and_dim(color,brightness)

    sm.put(ar, 8) # pushes a word of data to the state machine
    # second parameter indicates a shift value for each pushed data (from ar).
    # data is coded with 32 bits, so the value pushes the 24 bits at the right position.

# FUNCTION: Clear the neopixel ring (set all pixels to black)
def clear_light():
    ring=[BLACK]*NUM_LEDS # complete ring
    draw_ring(ring, NUM_LEDS)

# FUNCTION: Neopixel display modes
def neopixel_fixed_display(ring):
    draw_ring(ring, NUM_LEDS)

# FUNCTION: Neopixel flashed display
def neopixel_flashed_display(ring1,ring2):
    draw_ring(ring2, NUM_LEDS)
    time.sleep(0.005)
    draw_ring(ring1, NUM_LEDS)

# FUNCTION: Neopixel animated display
def neopixel_animated_display(n, ring1, ring2):
    if (n % 2) == 0:
        draw_ring(ring1, NUM_LEDS)
    else:
        draw_ring(ring2, NUM_LEDS)

#endregion ----------------------------------------------------------------------------------


#region: PROGRAM FOR TESTING PURPOSES ONLY --------------------------------------------------

if __name__ == "__main__":
    #neopixel_temp()
    #neopixel_humidity()
    #neopixel_pressure()
    #neopixel_wind_speed()
    #neopixel_few_clouds()
    #neopixel_clouds()
    #neopixel_thunderstorm()
    #neopixel_atmosphere()
    
    n = 0
    for i in range(10):
        n +=1
        #neopixel_drizzle(n)
        #neopixel_snow(n)
        #neopixel_rain(n)
        #neopixel_sunshine(n)
        #neopixel_moon(n)
        time.sleep(0.5)

#endregion ----------------------------------------------------------------------------------