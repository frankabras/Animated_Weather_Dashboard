# -------------------------------------------------------------------------------------------
# File : datas_logging.py
# Desc : This file contains functions to update and log weather data
# -------------------------------------------------------------------------------------------

import urequests, network
from logging import *
from hardware_setup import *
import utime

#region: FUNCTIONS DEFINITION ---------------------------------------------------------------
# FUNCTION: Uptade weather data from OpenWeatherMap API with hhtps request
def data_update(lcd, lon, lat):                                                            # QUESTIONABLE: wlan argument not used ?
    # Display update in progress on LCD
    lcd.clear()
    lcd.move_to(0,0)
    lcd.putstr("Updating data...")

    # Query OpenWeatherMap API for weather data
    root_url = "https://api.openweathermap.org/data/2.5/forecast?"
    url = root_url+"lat="+lat+"&lon="+lon+"&appid=" \
        +my_logging["OWM_API_key"]+"&units=metric"
    r = urequests.get(url)

    # Display update is done on LCD
    lcd.clear()
    lcd.move_to(0,0)
    lcd.putstr("  Data updated")
    utime.sleep(0.5)
    lcd.clear()

    return r

# FUNCTION: Log weather data from OpenWeatherMap API
def data_logging(r,time):
    # Conversion of json data into a dictionnary
    dict = r.json()
    
    # Logging data into a list for further use
    weather_forecast     = [None]*12
    weather_forecast[0]  = dict["city"]["name"]
    weather_forecast[1]  = dict["list"][time]["weather"][0]["main"]
    weather_forecast[2]  = dict["list"][time]["weather"][0]["description"]
    weather_forecast[3]  = dict["list"][time]["sys"]["pod"]
    weather_forecast[5]  = int((dict["list"][time]["pop"])*100)
    weather_forecast[6]  = round(float((dict ["list"][time]["main"]["temp"])),2)
    weather_forecast[7]  = round(float((dict["list"][time]["main"]["humidity"])),2)
    weather_forecast[8]  = round(float((dict["list"][time]["main"]["pressure"])),2)
    weather_forecast[9]  = round(float((dict["list"][time]["wind"]["speed"])*3.6),2)
    weather_forecast[10] = int((dict["list"][time]["wind"]["deg"]))
    weather_forecast[11] = round(float((dict["list"][time]["wind"]["gust"])*3.6),2)
    
    return weather_forecast

#endregion ----------------------------------------------------------------------------------


#region: PROGRAM FOR TESTING PURPOSES ONLY --------------------------------------------------

if __name__ == "__main__":
    # Setup
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
    
    
    wlan = network.WLAN(network.STA_IF) # Creates a WLAN object and initializes it
    wlan.active(True)
    wlan.connect(my_logging["ssid"],my_logging["WiFi_pass"])
    
    # Display connection info
    print("Connection to WiFi network.")
    print("---------------------------")
    print("Trying to connect to WiFi...")
    print()

    # Checking WiFi connection status
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

    # Display connection info
    print()
    print('Connected to WiFi network: ',end="")
    print(wlan.config("ssid"))
    print()
    ip=wlan.ifconfig()
    print("IP info (IP address, mask, gateway, DNS):")
    print(ip)
    print()
    
    # Data update and logging
    r = data_update(wlan, lcd)
    weather_forecast = data_logging(r,0)
    
    # Displaying logged data in the console
    print("Weather forecast from openweathermap.org")
    print("----------------------------------------")
    print("Location:",weather_forecast[0])
    print("Location:",dict["list"][0]["dt"])  #Convertir exemple : 1670598000
    print("Type of weather: ",weather_forecast[1])
    print("Descprition of weather: ",weather_forecast[2])
    print("Rain probability: ",round(weather_forecast[3]*100,1),"%")
    print("Current temperature: ",round(weather_forecast[4]-273.15,1),"°C")
    print("Minimum temperature today: ",round(weather_forecast[5]-273.15,1),"°C")
    print("Maximum temperature today: ",round(weather_forecast[6]-273.15,1),"°C")
    print("Relative humidity: ",round(weather_forecast[7]),"%")
    print("Atmospheric pressure: ",round(weather_forecast[8]),"hPa")
    print("Wind speed ",round(weather_forecast[9]),"m/s")
    print("Wind gust ",round(weather_forecast[11]),"m/s")
    print("Wind direction ",round(weather_forecast[10]),"°")

    #endregion ----------------------------------------------------------------------------------
