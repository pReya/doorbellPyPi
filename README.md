# doorbellPyPi
This is a simple python script to make your doorbell into an IoT doorbell that can send out push notifications when it's activated.

This script is supposed to run on a Raspberry Pi. It features two different inputs for two doorbells (e.g. one downstairs at your house entrance, one on your apartment door). Both inputs are high active (rising edge when bell is pressed). It uses threaded interrupts instead of a polling method to be efficient. It also uses a software debouncing mechanism so that the doorbell can be directly attached without the use of additional resistors or other measures to avoid interference.
