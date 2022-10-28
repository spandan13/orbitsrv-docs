# **Display RaspberryPi stats on I2C OLED Display**

> Display used: [0.96" OLED Display Module](https://robu.in/product/0-96-oled-display-module-spii2c-128x64-7-pin-blue/)  

## Clone the python script :
```
wget https://raw.githubusercontent.com/spandan13/pi-hosted/main/OLED-Stats/stats.py
```
## Start script at boot :
I'm using a simple cron job to do this.

` crontab -e `

Add the following line

` @reboot cd /path-to-script/ && python3 stats.py `






