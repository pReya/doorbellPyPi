#!/usr/bin/env python

from time import sleep, strftime, localtime
import os
import httplib, urllib
import RPi.GPIO as GPIO
import config


# Port setup
GPIO.setmode(GPIO.BCM)
GPIO.setup(config.BELL_1_PORT, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(config.BELL_2_PORT, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

# Pushover integration
def PushOver(title,message,url):

    #Connect with the Pushover API server
    conn = httplib.HTTPSConnection("api.pushover.net:443")

    #Send a POST request in urlencoded json
    conn.request("POST", "/1/messages.json",
        urllib.urlencode({
        "token": config.PUSHOVER_APP_KEY,
        "user": config.PUSHOVER_USER_KEY,
        "title": title,
        "message": message,
        "url": url,
        }), { "Content-type": "application/x-www-form-urlencoded" })

    #Any error messages or other responses?
    conn.getresponse()

def doorbellPush(channel):
    sleep(0.1)

    if GPIO.input(channel):

        # Bell upstairs
        if channel == config.BELL_1_PORT:
            description = config.BELL_1_DESCRIPTION

        # Bell downstairs
        elif channel == config.BELL_2_PORT:
            description = config.BELL_2_DESCRIPTION

        PushOver("%s (%s)" % (config.APP_TITLE, description),(config.BELL_MSG % description),"")
        print (config.CURR_TIME + " -- " + config.BELL_MSG % description) 


# Initialize
PushOver(config.APP_TITLE,config.ACTIVATION_MSG,"")
print (config.CURR_TIME + " -- " + config.ACTIVATION_MSG)

# Start event detection
GPIO.add_event_detect(config.BELL_1_PORT, GPIO.RISING, callback=doorbellPush, bouncetime=config.BOUNCETIME)
GPIO.add_event_detect(config.BELL_2_PORT, GPIO.RISING, callback=doorbellPush, bouncetime=config.BOUNCETIME)

try:
    while True:
        sleep(5.0)

# Kill 
except KeyboardInterrupt:
    PushOver(config.APP_TITLE,config.DEACTIVATION_MSG,"")
    print (config.CURR_TIME + " -- " + config.DEACTIVATION_MSG)
    GPIO.cleanup()


