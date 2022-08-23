import time
from telegram.ext import *
import gpiozero as gz

def rpi_temp():
    cpu_temp = os.popen("vcgencmd measure_temp").readline()
    return cpu_temp.replace("temp=", "")

API_KEY = "" #Add telegram bot API Key here
userid = "" # Add telegram userid here
updater = Updater(API_KEY, use_context=True)
   
temp = round((gz.CPUTemperature().temperature), 1)
if float(temp) > 55.0:

    message = "🔴 Current CPU Temp = " + str(temp) + "'C"
    updater.bot.send_message(userid, message)
