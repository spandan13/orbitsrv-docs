# **Display RaspberryPi stats on I2C OLED Display**

> Display used: [0.96" OLED Display Module](https://robu.in/product/0-96-oled-display-module-spii2c-128x64-7-pin-blue/)


## Initial Set-up for the Display :
* [Follow this guide](https://www.the-diy-life.com/add-an-oled-stats-display-to-raspberry-pi-os-bullseye/)

## Get the python script :
```
wget https://raw.githubusercontent.com/spandan13/pi-hosted/main/OLED-Stats/stats.py
```
## Start script at boot :

` crontab -e `

Add the following line

` @reboot && python3 /path-to-script/stats.py & `






