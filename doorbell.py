#!/usr/bin/env python

from time import sleep, strftime, localtime
import os
import httplib, urllib
import RPi.GPIO as GPIO

# Constants
APP_TITLE = "Klingel"
ACTIVATION_MSG = "Scharf gestellt"
DEACTIVATION_MSG = "Ueberwachung deaktiviert"
BELL_MSG = "Es hat %s geklingelt!"

CURR_TIME = strftime("%d.%m.%Y %H:%M:%S", localtime())

BELL_1_PORT = 25
BELL_1_DESCRIPTION = "unten"

BELL_2_PORT = 24
BELL_2_DESCRIPTION = "oben"

BOUNCETIME = 3000

PUSHOVER_APP_KEY = "XXX"
PUSHOVER_USER_KEY = "XXX"


# Port setup
GPIO.setmode(GPIO.BCM)
GPIO.setup(BELL_1_PORT, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(BELL_2_PORT, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

# Pushover integration
def PushOver(title,message,url):

    #Connect with the Pushover API server
    conn = httplib.HTTPSConnection("api.pushover.net:443")

    #Send a POST request in urlencoded json
    conn.request("POST", "/1/messages.json",
        urllib.urlencode({
        "token": PUSHOVER_APP_KEY,
        "user": PUSHOVER_USER_KEY,
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
        if channel == BELL_1_PORT:
            description = BELL_1_DESCRIPTION

        # Bell downstairs
        elif channel == BELL_2_PORT:
            description = BELL_2_DESCRIPTION

        PushOver("%s (%s)" % (APP_TITLE, description),(BELL_MSG % description),"")
        print (CURR_TIME + " -- " + BELL_MSG % description) 


# Initialize
PushOver(APP_TITLE,ACTIVATION_MSG,"")
print (CURR_TIME + " -- " + ACTIVATION_MSG)

# Start event detection
GPIO.add_event_detect(BELL_1_PORT, GPIO.RISING, callback=doorbellPush, bouncetime=BOUNCETIME)
GPIO.add_event_detect(BELL_2_PORT, GPIO.RISING, callback=doorbellPush, bouncetime=BOUNCETIME)

try:
    while True:
        sleep(5.0)

# Kill 
except KeyboardInterrupt:
    PushOver(APP_TITLE,DEACTIVATION_MSG,"")
    print (CURR_TIME + " -- " + DEACTIVATION_MSG)
    GPIO.cleanup()

