# -------------------------------------------------------------------------------------------
# File : hardware_setup.py
# This file contains functions to initialize and control hardware devices
# -------------------------------------------------------------------------------------------

from machine import Pin, ADC, I2C, PWM
from logging import *
from color_map import *
import network
import array, time,utime
import rp2
import pico_i2c_lcd

#region: GLOBAL CONSTANTS AND VARIABLES -----------------------------------------------------

# ===== VARIABLES ===========================================================================
# Variable to store old potentiometer value
oldPotValue = 0;

#endregion ----------------------------------------------------------------------------------


#region: FUNCTIONS DEFINITION ---------------------------------------------------------------

# ===== FUNCTIONS FOR HARDWARE SETUP ========================================================
# FUNCTION: Hardware initialization and WiFi connection
def hardware_setup():    
    # ##### HARDWARE SETUP ##################################################################

    # I2C and LCD initialization
    i2c = I2C(0, sda=Pin(8), scl=Pin(9), freq=400000)       # I2C initialization
    lcd = pico_i2c_lcd.I2cLcd(i2c, 0x27, 2, 16)             # LCD initialization 
    lcd.backlight_on()
    bckl = PWM(Pin(15))                                     # Backlight initialization
    bckl.freq(1000)
    bckl.duty_u16(32768)                                    # Backlight to maximum

    # Display hardware setup is starting message on LCD
    lcd.move_to(0,0)
    lcd.putstr(" Hardware setup")
    utime.sleep(0.5)
      
    # Servo initialization
    servo = PWM(Pin(22))
    servo.freq(50)
    
    # Potentiometer initialization
    pot = ADC(0)                                            # Connected to pin 26
    
    # Button initialization
    BP_menu = Pin(12, Pin.IN)
    
    # LED alerts initialization
    LED_freezingAlert = Pin(2, Pin.OUT)                     # White led
    LED_rainAlert = Pin(3, Pin.OUT)                         # Blue led
    LED_windAlert = Pin(4, Pin.OUT)                         # Yellow led
    LED_heatAlert = Pin(5, Pin.OUT)                         # Red led
    
    # Display setup done message on LCD
    lcd.clear()
    lcd.move_to(0,1)
    lcd.putstr("Setup is done!")
    utime.sleep(0.5)
    
    # ##### WIFI CONNECTION #################################################################

    # Display WiFi connection message on LCD
    lcd.clear()
    lcd.move_to(0,0)
    lcd.putstr("WiFi Connection")

    # Create and connect WLAN object
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    wlan.connect(my_logging["ssid"],my_logging["WiFi_pass"])
    
    # Checking WiFi connection status
    retry = 10
    while (retry > 0):
        wlan_stat=wlan.status()
        if wlan_stat==3:
            lcd.clear()
            lcd.move_to(0,0)
            lcd.putstr("     Got IP")
            break
        if wlan_stat==-1:
            lcd.clear()
            lcd.move_to(0,0)
            lcd.putstr("WiFi Connection:")
            lcd.move_to(0,1)
            lcd.putstr("    Failed !")
        if wlan_stat==-2:
            lcd.clear()
            lcd.move_to(0,0)
            lcd.putstr("No AP found")   
        if wlan_stat==-3:
            lcd.clear()
            lcd.move_to(0,0)
            lcd.putstr("Wrong WiFi")
            lcd.move_to(0,1)
            lcd.putstr("    password")
    
        if wlan.status() < 0 or wlan.status() >= 3:
            break
        retry = retry-1
        utime.sleep(1)
    utime.sleep(5)
    
    return (
        wlan,
        lcd,
        bckl,
        servo,
        pot,
        BP_menu,
        LED_freezingAlert,
        LED_rainAlert,
        LED_windAlert,
        LED_heatAlert
    )

# ===== FUNCTIONS FOR HARDWARE CONTROL ======================================================
# FUNCTION: Read the value of the potentiometer and display the selected time range on LCD
def read_time_selector(pot,lcd):
    # Select time range based on potentiometer value
    potValue = int(pot.read_u16()/1650)
    hour = int((potValue % 8) * 3)
    day = int(potValue / 8)
    
    # Display selected time range on LCD if changed
    global oldPotValue
    if oldPotValue != potValue:
        lcd.clear()
        if day == 0 and hour == 0:
            lcd.move_to(0,0)
            lcd.putstr("Now")
        elif day == 0:
            msgHours = "In",hour,"hours"                                                        # QUESTIONABLE : What is this line for ?
            lcd.move_to(0,0)
            lcd.putstr("In")
            lcd.move_to(3,0)
            lcd.putstr(str(hour))
            lcd.move_to(6,0)
            lcd.putstr("hours")
        else:
            lcd.move_to(0,0)
            lcd.putstr("In")
            lcd.move_to(3,0)
            lcd.putstr(str(day))
            lcd.move_to(5,0)
            lcd.putstr("day(s)")
            lcd.move_to(0,1)
            lcd.putstr("and")
            lcd.move_to(4,1)
            lcd.putstr(str(hour))
            lcd.move_to(7,1)
            lcd.putstr("hours")
        utime.sleep(1)
        lcd.clear()
    
    # Save current potentiometer value
    oldPotValue = potValue

    return potValue

    
# FUNCTION: Set the position of the servo according to the selected parameter
def set_servo_position(servo,position):
    if position <= 0:
        servo.duty_u16(8500)
        utime.sleep(0.01)
    elif position == 1:
        servo.duty_u16(8000)
        utime.sleep(0.01)
    elif position == 2:
        servo.duty_u16(7250)
        utime.sleep(0.01)
    elif position == 3:
        servo.duty_u16(6520)
        utime.sleep(0.01)
    elif position == 4:
        servo.duty_u16(5860)
        utime.sleep(0.01)
    elif position == 5:
        servo.duty_u16(5200)
        utime.sleep(0.01)
    elif position == 6:
        servo.duty_u16(4500)
        utime.sleep(0.01)
    elif position == 7:
        servo.duty_u16(3850)
        utime.sleep(0.01)
    elif position == 8:
        servo.duty_u16(3250)
        utime.sleep(0.01)
    elif position == 9:
        servo.duty_u16(2500)
        utime.sleep(0.01)
    elif position >= 10:
        servo.duty_u16(1900)
        utime.sleep(0.01)


#endregion ----------------------------------------------------------------------------------


#region: PROGRAM FOR TESTING PURPOSES ONLY --------------------------------------------------

if __name__ == "__main__":
    (
        wlan,
        lcd,
        bckl,
        servo,
        pot,
        menuButton,
        LED_freezingAlert,
        LED_rainAlert,
        LED_windAlert,
        LED_heatAlert
    ) = hardware_setup()
    
    print("Connection to WiFi network.")
    print("---------------------------")
    print("Trying to connect to WiFi...")
    print()
    
    # Waits for connection or exit with error code if it fails
    retry = 10
    while (retry > 0):
        wlan_stat=wlan.status()
        if wlan_stat==3:
            print("Got IP")
            break
        if wlan_stat==-1:
            raise RuntimeError('WiFi connection failed')
        if wlan_stat==-2:
            raise RuntimeError('No AP found')    
        if wlan_stat==-3:
            raise RuntimeError('Wrong WiFi password')
    
        if wlan.status() < 0 or wlan.status() >= 3:
            break
        retry = retry-1
        utime.sleep(1)

    if wlan_stat!=3:
        raise RuntimeError('WiFi connection failed')

    print()
    print('Connected to WiFi network: ',end="")
    print(wlan.config("ssid"))
    print()
    ip=wlan.ifconfig()
    print("IP info (IP address, mask, gateway, DNS):")
    print(ip)
    print()

#endregion ----------------------------------------------------------------------------------