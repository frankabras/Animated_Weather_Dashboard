# Animated_Weather_Dashboard
Animated Weather Dashboard is an interactive and animated weather dashboard prototype, developed to display weather forecasts over a configurable time range. This project uses a Raspberry Pi Pico W to fetch real-time data via the OpenWeatherMap API and visualize it in a visual and intuitive way.

## Key Features

* Weather data display: temperature, humidity, wind speed/direction, gusts, atmospheric pressure, and forecasts (clouds, rain, snow, etc.),
* Time range selection (up to 5 days in 3-hour steps) via potentiometer and menu via button,
* LED alerts for extreme conditions: frost, heatwaves, strong winds, heavy precipitation.

## Hardware 

* Raspberry Pi Pico W,
* NeoPixel ring (16 LEDs) for colored indicators and animations,
* 16x2 LCD screen,
* Servo motor (analog gauge),
* 4 alert LEDs,
* Button,
* Potentiometer.

## Software Architecture
The MicroPython code is modular:

* `main.py`: orchestration of timers and interrupts,
* `hardware_setup.py`: initialization of WiFi, LCD, servo, etc,
* `neopixel_ring.py`: NeoPixel animations with PIO,
* `data_logging.py`: API data retrieval and JSON parsing,
* `display_data.py`: multi-modal displays and alerts.
