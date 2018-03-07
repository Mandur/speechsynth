import pyttsx3
import os
import json
from sender import Sender

def do_speech_synth(engine,sentence):
    engine.say(sentence)
    engine.runAndWait() 

def main():
    engine = pyttsx3.init()
    rate = engine.getProperty('rate')
    engine.setProperty('rate', rate-30)
    engine.setProperty('voice', 'english+f4')
  
    # These variables are set by the IoT Edge Agent
    CONNECTION_STRING = os.getenv('EdgeHubConnectionString')
    CA_CERTIFICATE = os.getenv('EdgeModuleCACertificateFile', False)
    sender = Sender(CONNECTION_STRING, CA_CERTIFICATE)
    print("connected to "+CONNECTION_STRING)
    do_speech_synth(engine,"Synthethizer online")
    sender.receive_message(on_message_received,'receive')

def on_message_received():
    print("12")
    do_speech_synth(engine,"Initialized")


if __name__ == "__main__":
    main()
