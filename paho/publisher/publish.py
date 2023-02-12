import paho.mqtt.client as mqtt
import time

# to create dummy data
import random

# to read sensor data
#from adafruit_dht import read

# ------------------------ PUBLISH  FUNCTIONS ------------------------ #
from config import BROKER_HOST, BROKER_PORT, BROKER_KEEPALIVE, BROKER_USER, BROKER_PASS
from config import TOPIC_TEMPERATURE, TOPIC_HUMIDITY
from config import SLEEP, MODEL, PIN

from util import get_current_time as now

from callbacks import on_log, on_connect, on_disconnect, on_publish

def send_payload():
    next = "temperature"
        
    while True:
        print(f"[{now()}] ------------------ new reading publishing ------------------")
        
        # from sensor
        # -----------
        #temperature = read(MODEL, PIN, measure='temperature')
        #humidity    = read(MODEL, PIN, measure='humidity')

        # random dummy data generation 
        # ----------------------------
        # temperature -> (25 ~ 35) *C & 
        # humidity -> (35 - 45) %
        #temperature = random.uniform(25.00, 35.00)
        #humidity = random.uniform(35.00, 45.00)

        # rounding 1 precisioin point:
        # ----------------------------
        # procedure 1
        #temperature = float("%.1f" % temperature)
        #humidity    = float("%.1f" % humidity)
        # procedure 2
        #temperature = round(temperature, 1)            
        #humidity    = round(humidity, 1)

        measurement = next

        if next == "temperature":
            # topic
            # ---------------------------------------------------
            topic = TOPIC_TEMPERATURE

            # data
            # --------------------------------------------------- 
            # -- from real sensor
            #temperature = read(MODEL, PIN, measure='temperature')
            # -- artificially generated
            temperature = random.uniform(25.00, 35.00)
            payload = round(temperature, 1)
            isSleepRequired = False
            next = "humidity"
        else:
            # topic
            # ---------------------------------------------------
            topic = TOPIC_HUMIDITY

            # data
            # --------------------------------------------------- 
            # -- from real sensor
            #humidity    = read(MODEL, PIN, measure='humidity')
            # -- artificially generated
            humidity = random.uniform(35.00, 45.00)
            payload    = round(humidity, 1)
            isSleepRequired = True
            next = "temperature"
        
        print(f"[{now()}]  topic: %s " % topic)
        print(f"[{now()}]  {measurement}: %.1f " % payload) 
        client.publish(topic, payload)
            
        print(f"[{now()}] --------------------------- done ---------------------------")
        
        if isSleepRequired:
            time.sleep(SLEEP)
# ------------------------------- ENDS ------------------------------- #


if __name__ == '__main__':

    try:
        # Create an MQTT client and attach our routines to it.
        #client              = mqtt.Client(BROKER_ID)
        client              = mqtt.Client()
        
        # built-in callbacks
        client.on_log       = on_log
        client.on_connect   = on_connect

        client.username_pw_set(BROKER_USER, BROKER_PASS)
        client.connect(BROKER_HOST, BROKER_PORT, BROKER_KEEPALIVE)
        
        client.loop_start()
        send_payload()

    except KeyboardInterrupt:
        # disconnect
        # client.on_disconnect  = on_disconnect
        client.disconnect() 
