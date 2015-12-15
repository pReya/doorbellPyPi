# doorbellPyPi
This is a simple python script to make your doorbell into an IoT doorbell that can send out push notifications to your smartphone when it's activated.

This script is supposed to run on a Raspberry Pi. It features two different inputs for two doorbells (e.g. one downstairs at your house entrance, one on your apartment door).

## Features
* Push Notifications make use of [PushOver](https://pushover.net/)
* Configuration through variables in the header section
* Strings are completely customizable – Standard language is German
* Doorbell(s) are connected through two customizable high active (high = pressed) GPIO inputs on the Raspberry Pi
* Push Notifications are triggered by hardware interrupts
* Software debouncing so there is no need for hardware debouncing of any kind (though it's always a good idea to do it anyway)
* Additionally all events are written to the system console

## Installation / configuration

1. Configure all Strings in the header are to your liking
2. Choose the correct RPi GPIO Input pins (BCM numbering)
3. Insert your PushOver App and User (or Group) Key
4. Start the script (it will stop after some time if it is run through a regular SSH session. I'd recommend using "screen" to keep it running in the background)