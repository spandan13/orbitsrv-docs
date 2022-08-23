import time
from telegram.ext import *
import gpiozero as gz


API_KEY = "" #Add telegram bot API Key here
userid = "" # Add telegram userid here
temp_limit = 70.0 # Change to your prefered limit


updater = Updater(API_KEY, use_context=True)  
temp = round((gz.CPUTemperature().temperature), 1)
if float(temp) > temp_limit:

    message = "🔴 Current CPU Temp = " + str(temp) + "'C"
    updater.bot.send_message(userid, message)
