# -------------------------------------------------------------------------------------------
# File : main.py
# Desc : Main program file for Animated Weather Dashboard 
# -------------------------------------------------------------------------------------------

import sys
sys.path.append('lcd')
from hardware_setup import *
from datas_logging import *
from display_datas import *
from machine import Pin, Timer

#region: GLOBAL CONSTANTS AND VARIABLES -----------------------------------------------------

# ===== CONSTANTS ===========================================================================
location = ["5.581565690222564", "50.6202012460474"]    # [longitude, latitude]

# ===== VARIABLES ===========================================================================
menuCounter = 0                                         # Menu counter for display 
timeSelector = 0                                        # Time selector for weather data

# ===== TIMERS ===============================================================================
timer1 = Timer()                                        # Display data timer
timer2 = Timer()                                        # Potentiometer reading timer
timer3 = Timer()                                        # Update data timer

#endregion ----------------------------------------------------------------------------------


#region: FUNCTIONS DEFINITION ---------------------------------------------------------------

# ===== FUNCTIONS FOR INTERRUPTS ============================================================
# FUNCTION: Change menu on button press
def menu_change(Pin):
    global menuCounter
    menuCounter += 1
    if menuCounter > 5:
        menuCounter = 0
    print("menu increased")
    print("menu : ",menuCounter)

# ===== FUNCTIONS FOR TIMERS ================================================================
# FUNCTION: Select time for weather data based on potentiometer value
def time_selector(timer):
    global timeSelector
    timeSelector = read_time_selector(pot,lcd)
    
# FUNCTION: Update weather data from OpenWeatherMap API
def uptade_weather(timer):                                                                      # CHANGE: function name typo
    global r
    r = data_update(wlan,lcd, location[0], location[1])

# FUNCTION: Display weather data and alerts
def display_weather(timer):
    weather_forecast = data_logging(r,timeSelector)
    display_data(menuCounter,weather_forecast,lcd,servo)
    display_alerts(weather_forecast,LED_freezingAlert,LED_rainAlert,LED_windAlert,LED_heatAlert)

#endregion ----------------------------------------------------------------------------------


#region: MAIN PROGRAM -----------------------------------------------------------------------

# ===== Initializations =====================================================================
# Setup
wlan,lcd,bckl,servo,pot,menuButton,LED_freezingAlert,LED_rainAlert,LED_windAlert,LED_heatAlert = hardware_setup()  # CHANGE: line length

# Datas logging
r = data_update(wlan,lcd, location[0], location[1])
weather_forecast = data_logging(r,timeSelector)

# Datas display
display_data(menuCounter,weather_forecast,lcd,servo)
display_alerts(weather_forecast,LED_freezingAlert,LED_rainAlert,LED_windAlert,LED_heatAlert)
lcd.clear()

# ===== TIMER AND INTERRUPTS SETUP ==========================================================
# Timers interruptions
timer1.init(freq=2, mode=Timer.PERIODIC, callback=display_weather)
timer2.init(freq=2, mode=Timer.PERIODIC, callback=time_selector)
timer3.init(freq=0.00167, mode=Timer.PERIODIC, callback=uptade_weather)

# GPIO interruption
menuButton.irq(trigger=Pin.IRQ_FALLING, handler=menu_change)

#endregion ----------------------------------------------------------------------------------