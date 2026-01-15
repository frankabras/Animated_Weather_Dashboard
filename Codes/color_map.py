# -------------------------------------------------------------------------------------------
# File : color_map.py
# Desc : This file contains several colors and color maps used for neopixel ring
# -------------------------------------------------------------------------------------------

#region: COLORS DEFINITION ------------------------------------------------------------------

# ===== BLUE ================================================================================
# Common blue shades
BLUE = (0,0,255)
MIDNIGHT_BLUE = (0,0,50)
NAVY = (0,0,25)
MEDIUM_BLUE = (0,0,205) 
ROYAL_BLUE = (50,50,225)
CORNFLOWER_BLUE = (100,120,237)
LIGHT_SKY_BLUE = (135,206,250)

# Personal blue shades
BLUE1 = (25,25,255)
BLUE2 = (50,50,255)
BLUE3 = (75,75,255)
BLUE4 = (100,100,255)

# ===== YELLOW ==============================================================================
# Common yellow shades
LIGHT_YELLOW = (255,255,65)
CORN_SILK = (255,248,220)
YELLOW = (255,255,0)
GOLD = (255,215,0)

# Personal yellow shades
YELLOW1 = (75,75,0)

# ===== ORANGE ==============================================================================
# Common orange shades
LIGHT_ORANGE = (255,190,0)
ORANGE = (255,90,0)
DARK_ORANGE = (255,140,0)
CHOCOLATE = (210,105,30)

# ===== RED =================================================================================
# Common red shades
TOMATO = (255,99,71)
ORANGE_RED = (255,69,0)
RED = (255,0,0)
CRIMSON = (220,20,60)
DARK_RED = (50,0,0)

# Personal red shades
RED1 = (255,25,25)
RED2 = (255,50,50)
RED3 = (255,75,75)
RED4 = (255,100,100)

# ===== GREEN ===============================================================================
# Common green shades
GREEN = (0,255,0)

# Personal green shades
GREEN1 = (25,255,25)
GREEN2 = (50,255,50)
GREEN3 = (75,255,75)
GREEN4 = (100,255,100)

# ===== GRAYSCALE ===========================================================================
WHITE = (255,255,255)
GREY = (50,50,50)
BLACK = (0, 0, 0)

# ===== OTHERS ==============================================================================
PURPLE = (128,0,128)

#endregion ----------------------------------------------------------------------------------


#region: COLOR MAPS DEFINITION --------------------------------------------------------------

# Ring temperature
RING_TEMPERATURE = [MIDNIGHT_BLUE,BLUE,ROYAL_BLUE,CORNFLOWER_BLUE,WHITE,LIGHT_YELLOW,LIGHT_ORANGE,ORANGE_RED, \
                    RED,DARK_RED,BLACK,BLACK,BLACK,BLACK,BLACK,BLACK]

# Ring humidity
RING_HUMIDITY = [WHITE,WHITE,BLUE4,BLUE3,BLUE2,BLUE2,BLUE1,BLUE1, \
                 MIDNIGHT_BLUE,MIDNIGHT_BLUE,BLACK,BLACK,BLACK,BLACK,BLACK,BLACK]

# Ring pressure
RING_PRESSURE = [MIDNIGHT_BLUE,BLUE1,BLUE2,BLUE3,BLUE4,WHITE,RED3,RED2, \
                   RED1,BLACK,BLACK,BLACK,BLACK,BLACK,BLACK,BLACK]

# Ring wind speed/gust
RING_WIND_SPPED = [GREEN,GREEN1,GREEN2,GREEN3,GREEN4,WHITE,RED3,RED2, \
                   RED1,RED,BLACK,BLACK,BLACK,BLACK,BLACK,BLACK]

# Ring air quality
RING_AIR_Q = [DARK_RED,DARK_RED,ORANGE,ORANGE,YELLOW,YELLOW,GREEN,GREEN,BLUE,BLUE,BLACK,BLACK,BLACK,BLACK,BLACK,BLACK]

# Rings sunshine
RING_SUNSHINE_1 = [LIGHT_ORANGE,ORANGE_RED,LIGHT_ORANGE,ORANGE_RED,LIGHT_ORANGE,ORANGE_RED,LIGHT_ORANGE,ORANGE_RED, \
                   LIGHT_ORANGE,ORANGE_RED,LIGHT_ORANGE,ORANGE_RED,LIGHT_ORANGE,ORANGE_RED,LIGHT_ORANGE,ORANGE_RED]
RING_SUNSHINE_2 = [ORANGE_RED,LIGHT_ORANGE,ORANGE_RED,LIGHT_ORANGE,ORANGE_RED,LIGHT_ORANGE,ORANGE_RED,LIGHT_ORANGE, \
                   ORANGE_RED,LIGHT_ORANGE,ORANGE_RED,LIGHT_ORANGE,ORANGE_RED,LIGHT_ORANGE,ORANGE_RED,LIGHT_ORANGE]
# Rings moon
RING_MOON_1 = [GREY,WHITE,GREY,WHITE,GREY,WHITE,GREY,WHITE,GREY,WHITE,GREY,WHITE,GREY,WHITE,GREY,WHITE]
RING_MOON_2 = [WHITE,GREY,WHITE,GREY,WHITE,GREY,WHITE,GREY,WHITE,GREY,WHITE,GREY,WHITE,GREY,WHITE,GREY]

# Ring few clouds
RING_FEW_CLOUDS = [GREY,GREY,GREY,GREY,GREY,YELLOW,YELLOW,GREY, \
                   GREY,BLACK,BLACK,BLACK,BLACK,BLACK,BLACK,BLACK]

# Ring clouds
RING_CLOUDS = [GREY,GREY,GREY,GREY,GREY,GREY,GREY,GREY,GREY,BLACK,BLACK,BLACK,BLACK,BLACK,BLACK,BLACK]

# Ring rain
RING_DRIZZLE_1 = [BLACK,BLUE,BLACK,BLUE,BLACK,BLUE,BLACK,BLUE,BLACK,BLUE,BLACK,BLUE,BLACK,BLUE,BLACK,BLUE]
RING_DRIZZLE_2 = [BLUE,BLACK,BLUE,BLACK,BLUE,BLACK,BLUE,BLACK,BLUE,BLACK,BLUE,BLACK,BLUE,BLACK,BLUE,BLACK]

# Ring rain
RING_RAIN_1 = [GREY,GREY,GREY,GREY,GREY,GREY,GREY,GREY,GREY,BLUE,BLACK,BLUE,BLACK,BLUE,BLACK,BLUE]
RING_RAIN_2 = [GREY,GREY,GREY,GREY,GREY,GREY,GREY,GREY,GREY,BLACK,BLUE,BLACK,BLUE,BLACK,BLUE,BLACK]

# Rings thunderstorm
RING_STORMY_1 = [GREY,GREY,GREY,GREY,GREY,GREY,GREY,GREY,GREY,BLACK,BLACK,BLACK,BLACK,BLACK,BLACK,BLACK]
RING_STORMY_2 = [GREY,GREY,GREY,GREY,GREY,GREY,GREY,GREY, \
                 GREY,LIGHT_YELLOW,LIGHT_YELLOW,LIGHT_YELLOW,LIGHT_YELLOW,LIGHT_YELLOW,LIGHT_YELLOW,LIGHT_YELLOW]

# Ring snow
RING_SNOW_1 = [GREY,GREY,GREY,GREY,GREY,GREY,GREY,GREY,GREY,WHITE,BLACK,WHITE,BLACK,WHITE,BLACK,WHITE]
RING_SNOW_2 = [GREY,GREY,GREY,GREY,GREY,GREY,GREY,GREY,GREY,BLACK,WHITE,BLACK,WHITE,BLACK,WHITE,BLACK]

# Ring atmosphere
RING_ATMOSPHERE = [GREY,BLACK,GREY,BLACK,GREY,BLACK,GREY,BLACK,GREY,BLACK,GREY,BLACK,GREY,BLACK,GREY,BLACK]

#endregion ----------------------------------------------------------------------------------