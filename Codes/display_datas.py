# -------------------------------------------------------------------------------------------
# File : display_datas.py
# Desc : This file contains functions to display weather data on the LCD and control the
#        servo and neopixel ring
# -------------------------------------------------------------------------------------------
from hardware_setup import *
from datas_logging import *
from neopixel_ring import *

#region: GLOBAL CONSTANTS AND VARIABLES -----------------------------------------------------

# ===== VARIABLES ===========================================================================

# Counters for animated neopixel display
cntSunshine = 0
cntDrizzle = 0
cntRain = 0
cntSnow = 0

#endregion ----------------------------------------------------------------------------------


#region: FUNCTIONS DEFINITION ---------------------------------------------------------------

# ===== FUNCTIONS FOR DISPLAY ===============================================================
# FUNCTION: Display weather data through hardware components
def display_data(menuCounter,weather_forecast,lcd,servo):
    global cntSunshine,cntDrizzle,cntRain,cntSnow
    
    # Weather forecast
    if menuCounter == 0: 
        # LCD display
        lcd.move_to(0,0)
        lcd.putstr("Forecast:    ") #move to 11
        lcd.move_to(12,0)
        lcd.putstr(str(weather_forecast[5]))
        lcd.move_to(15,0)
        lcd.putstr("%")
        lcd.move_to(0,1)
        lcd.putstr("              ")
        lcd.move_to(0,1)
        lcd.putstr(weather_forecast[1])
        # Neopixel
        if weather_forecast[1] == "Clear":
            # Counter for animated display
            cntSnow = 0
            cntRain = 0
            cntDrizzle = 0
            cntSunshine += 1
            # Verification of the part of the day
            if weather_forecast[3] == 'n':
                neopixel_animated_display(cntSunshine,RING_MOON_1,RING_MOON_2)
            else:
                neopixel_animated_display(cntSunshine,RING_SUNSHINE_1,RING_SUNSHINE_2)
        elif weather_forecast[1] == "Clouds":
            # Verification if a lot or few clouds
            if weather_forecast[2] == "scattered clouds" or weather_forecast[2] == "few clouds":
                neopixel_fixed_display(RING_FEW_CLOUDS)
            else:
                neopixel_fixed_display(RING_CLOUDS)
        elif weather_forecast[1] == "Drizzle":
            # Counter for animated display
            cntSunshine = 0
            cntRain = 0
            cntSnow = 0
            cntDrizzle += 1
            neopixel_animated_display(cntDrizzle,RING_DRIZZLE_1,RING_DRIZZLE_2)
        elif weather_forecast[1] == "Rain":
            # Counter for animated display
            cntSunshine = 0
            cntDrizzle = 0
            cntSnow = 0
            cntRain += 1
            neopixel_animated_display(cntRain,RING_RAIN_1,RING_RAIN_2)
        elif weather_forecast[1] == "Snow":
            # Counter for animated display
            cntRain = 0
            cntDrizzle = 0
            cntSunshine = 0
            cntSnow += 1
            neopixel_animated_display(cntSnow,RING_SNOW_1,RING_SNOW_2)
        elif weather_forecast[1] == "Thunderstorm":
            neopixel_flashed_display(RING_STORMY_1,RING_STORMY_2)
        elif weather_forecast[1] == "Atmosphere":
            neopixel_fixed_display(RING_ATMOSPHERE)
        # Servo
        servoPosition = 0
        set_servo_position(servo,servoPosition)

    # Temperature
    elif menuCounter == 1:
        # LCD display
        lcd.move_to(0,0)
        lcd.putstr("Temperature:    ")
        lcd.move_to(0,1)
        lcd.putstr(str(weather_forecast[6])+" C     ")
        # Neopixel
        neopixel_fixed_display(RING_TEMPERATURE)
        # Servo
        servoPosition = int((weather_forecast[6]+10)/5)
        set_servo_position(servo,servoPosition)

    # Humidity
    elif menuCounter == 2:
        # LCD display
        lcd.move_to(0,0)
        lcd.putstr("Humidity:       ")
        lcd.move_to(0,1)
        lcd.putstr(str(weather_forecast[7])+"%     ")
        # Neopixel
        neopixel_fixed_display(RING_HUMIDITY)
        # Servo
        servoPosition = int(weather_forecast[7]/10)
        set_servo_position(servo,servoPosition)

    # Wind speed and direction
    elif menuCounter == 3:
        # LCD display
        direction = conv_wind_direction(weather_forecast[10])
        lcd.move_to(0,0)
        lcd.putstr(str("Wind speed:   "+direction))
        lcd.move_to(0,1)
        lcd.putstr(str(weather_forecast[9])+"km/h    ")
        # Neopixel
        neopixel_fixed_display(RING_WIND_SPPED)
        # Servo
        servoPosition = int(weather_forecast[9]/15)
        set_servo_position(servo,servoPosition)
        
    # Wind gust
    elif menuCounter == 4:
        # LCD display
        lcd.move_to(0,0)
        lcd.putstr("Wind gust:      ")
        lcd.move_to(0,1)
        lcd.putstr(str(weather_forecast[11])+"km/h    ")
        # Neopixel
        neopixel_fixed_display(RING_WIND_SPPED)
        # Servo
        servoPosition = int(weather_forecast[11]/15)
        set_servo_position(servo,servoPosition)

    # Atmospheric pressure
    elif menuCounter == 5:
        # LCD display
        lcd.move_to(0,0)
        lcd.putstr("Pressure:       ")
        lcd.move_to(0,1)
        lcd.putstr(str(weather_forecast[8])+"hPa    ")
        # Neopixel
        neopixel_fixed_display(RING_PRESSURE)
        # Servo
        servoPosition = int((weather_forecast[8]-970)/10)
        set_servo_position(servo,servoPosition)


# FUNCTION: Display alerts through LEDs
def display_alerts(weather_forecast,LED_freezingAlert,LED_rainAlert,LED_windAlert,LED_heatAlert):
    # Freezing alert
    if weather_forecast[6] <= 3 or weather_forecast[2] == "freezing rain":  
        LED_freezingAlert.value(1)
    else:
        LED_freezingAlert.value(0)
    # Heat alert
    if weather_forecast[6] >= 30:
        LED_heatAlert.value(1)
    else:
        LED_heatAlert.value(0)
    # Wind alert
    if weather_forecast[9] >= 80 or weather_forecast[11] >= 50:
        LED_windAlert.value(1)
    else:
        LED_windAlert.value(0)
    # Rain alert
    if weather_forecast[2] == "extreme rain" or weather_forecast[2] == "very heavy rain":
        LED_rainAlert.value(1)
    else:
        LED_rainAlert.value(0)

# ===== MISCELLANEOUS FUNCTIONS =============================================================
# FUNCTION: Convert wind direction in degrees to compass direction
def conv_wind_direction(directionDeg):
    # North
    if directionDeg >= 338 or directionDeg <= 22 :
        compass = "N"
    # North-East
    elif directionDeg >= 23 and directionDeg <= 67:
        compass = "NE"
    # East
    elif directionDeg >= 68 and directionDeg <= 112:
        compass = "E"
    # South-East
    elif directionDeg >= 113 and directionDeg <= 157:
        compass = "SE"
    # South
    elif directionDeg >= 158 and directionDeg <= 202:
        compass = "S"
    # South-West
    elif directionDeg >= 203 and directionDeg <= 247:
        compass = "SW"
    # West
    elif directionDeg >= 248 and directionDeg <= 292:
        compass = "W"
    # North-West
    elif directionDeg >= 293 and directionDeg <= 337:
        compass = "NW"
    
    return compass

#endregion ----------------------------------------------------------------------------------