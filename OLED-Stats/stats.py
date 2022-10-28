# Original Script created by: Michael Klements - https://github.com/mklements/OLED_Stats/blob/main/stats.py
# This is a modified version of the above script
# For Raspberry Pi Desktop Case with OLED Stats Display
# Base on Adafruit CircuitPython & SSD1306 Libraries
# Installation & Setup Instructions - https://www.the-diy-life.com/add-an-oled-stats-display-to-raspberry-pi-os-bullseye/
import time
import board
import busio
import digitalio

from PIL import Image, ImageDraw, ImageFont
import adafruit_ssd1306

import subprocess

# Define the Reset Pin
oled_reset = digitalio.DigitalInOut(board.D4)

# Display Parameters
WIDTH = 128
HEIGHT = 64
BORDER = 5

# Use for I2C.
i2c = board.I2C()
oled = adafruit_ssd1306.SSD1306_I2C(WIDTH, HEIGHT, i2c, addr=0x3C, reset=oled_reset)

# Clear display.
oled.fill(0)
oled.show()

# Create blank image for drawing.
# Make sure to create image with mode '1' for 1-bit color.
image = Image.new("1", (oled.width, oled.height))

# Get drawing object to draw on image.
draw = ImageDraw.Draw(image)

# Draw a white background
draw.rectangle((0, 0, oled.width, oled.height), outline=255, fill=255)

font = ImageFont.truetype('PixelOperator.ttf', 55)
font2 = ImageFont.truetype('PixelOperator.ttf', 16)

while True:

    # Draw a black filled box to clear the image.
    draw.rectangle((0, 0, oled.width, oled.height), outline=0, fill=0)

    # Shell scripts for system monitoring from here : https://unix.stackexchange.com/questions/119126/command-to-display-memory-usage-disk-usage-and-cpu-load
    cmd = "top -bn1 -p 1 | fgrep \"Cpu(s)\" | tail -1 | awk -F'id,' -v prefix=\"$prefix\" '{ split($1, vs, \",\"); v=vs[length(vs)]; sub(\"%\", \"\", v); printf \"%s%.1f%%\", prefix, 100 - v }'"
    CPU = subprocess.check_output(cmd, shell = True )
    cmd = "free --giga -h | awk 'NR==2{printf \"Mem: %s/%s\", $3,$2 }'"
    MemUsage = subprocess.check_output(cmd, shell = True )
    cmd = "vcgencmd measure_temp |cut -f 2 -d '='"
    temp = subprocess.check_output(cmd, shell = True )

    # Pi Stats Display
    draw.text((0, 12), "CPU:", font=font2, fill=255)
    draw.text((0, 16), str(CPU,'utf-8'), font=font, fill=255)
    draw.text((0, 0), str(MemUsage,'utf-8'), font=font2, fill=255)
        
    # Display image
    oled.image(image)
    oled.show()
    time.sleep(2)

    
    ##Switch to temps
    # Draw a black filled box to clear the image.
    draw.rectangle((0, 0, oled.width, oled.height), outline=0, fill=0)

    # Pi Stats Display
    draw.text((0, 12), "Temp:", font=font2, fill=255)
    draw.text((0, 16), str(temp,'utf-8') , font=font, fill=255)
    draw.text((0, 0), str(MemUsage,'utf-8'), font=font2, fill=255)

    # Display image
    oled.image(image)
    oled.show()
    time.sleep(2)
