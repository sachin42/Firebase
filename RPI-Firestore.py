import os
import firebase_admin
from firebase_admin import credentials
from google.cloud import firestore
from firebase_admin import firestore
import collections
from typing import Collection
from gpiozero import LED, Button, Buzzer, PWMLED

cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred)

led1 = LED(20)
led2 = PWMLED(21)
bz = Buzzer(17)

btn = Button(16)

db = firestore.client()

db-collections('outputDevices').document('digitalLED').set(
    {
        'status' : False
    }
)

db-collections('outputDevices').document('pwmLED').set(
    {
        'brightness' : 0
    }
)

db-collections('outputDevices').document('buzzer').set(
    {
        'alarm' : False
    }
)