from time import sleep, strftime, localtime

# Configuration
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
