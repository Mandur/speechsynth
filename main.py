import pyttsx3
import os
import time
import json
from sender import Sender



def do_speech_synth(sentence):
    engine.say(sentence)
    engine.runAndWait() 

def main():
    global engine
    engine = pyttsx3.init()
    rate = engine.getProperty('rate')
    engine.setProperty('rate', rate-30)
    engine.setProperty('voice', 'english+f4')
  
    # These variables are set by the IoT Edge Agent
    CONNECTION_STRING = os.getenv('EdgeHubConnectionString')
    CA_CERTIFICATE = os.getenv('EdgeModuleCACertificateFile', False)
    sender = Sender(CONNECTION_STRING, CA_CERTIFICATE)
    print("connected to "+CONNECTION_STRING)
    do_speech_synth("Synthethizer online")
    sender.receive_message(on_message_received,'receive')
    while True:
        time.sleep(1)
        print("finished sleeping")

def on_message_received(message,usercontext):
    print("I received a message")
    message_buffer = message.get_bytearray()
    print(message_buffer)
    do_speech_synth( message_buffer)


main()
