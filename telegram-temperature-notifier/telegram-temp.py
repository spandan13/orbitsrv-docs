import time
from telegram.ext import *
import gpiozero as gz

def rpi_temp():
    cpu_temp = os.popen("vcgencmd measure_temp").readline()
    return cpu_temp.replace("temp=", "")

API_KEY = ''
updater = Updater(API_KEY, use_context=True)
    
#while True:
    #temp = rpi_temp().replace("'C\n", "")
temp = round((gz.CPUTemperature().temperature), 1)
if float(temp) > 55.0:

    message = "🔴 Current CPU Temp = " + str(temp) + "'C"
    updater.bot.send_message("-619896582", message)
