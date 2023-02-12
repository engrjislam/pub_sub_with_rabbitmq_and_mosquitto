import paho.mqtt.client as mqtt
import time
import random

# ------------------------ PUBLISH  FUNCTIONS ------------------------ #
from config import BROKER_HOST, BROKER_PORT, BROKER_KEEPALIVE, BROKER_USER, BROKER_PASS
from config import TOPIC_TEMPERATURE, TOPIC_HUMIDITY
from config import SLEEP, MODEL, PIN

from util import get_current_time as now

from callbacks import on_log, on_connect, on_disconnect, on_publish


def send_payload():
    next_topic = "temperature"

    while True:
        print(f"[{now()}] ------------------ new reading publishing ------------------")

        measurement = next

        if next_topic == "temperature":
            # topic
            # ---------------------------------------------------
            topic = TOPIC_TEMPERATURE
            temperature = random.uniform(25.00, 35.00)
            payload = round(temperature, 1)
            isSleepRequired = False
            next_topic = "humidity"
        else:
            # topic
            # ---------------------------------------------------
            topic = TOPIC_HUMIDITY
            humidity = random.uniform(35.00, 45.00)
            payload = round(humidity, 1)
            isSleepRequired = True
            next_topic = "temperature"

        print(f"[{now()}]  topic: %s " % topic)
        print(f"[{now()}]  {measurement}: %.1f " % payload)
        client.publish(topic, payload, qos=0)

        print(f"[{now()}] --------------------------- done ---------------------------")

        if isSleepRequired:
            time.sleep(SLEEP)


if __name__ == "__main__":
    try:
        # Create an MQTT client and attach our routines to it.
        # client              = mqtt.Client(BROKER_ID)
        client = mqtt.Client()

        # built-in callbacks
        client.on_log = on_log
        client.on_connect = on_connect

        client.username_pw_set(BROKER_USER, BROKER_PASS)
        client.connect(BROKER_HOST, BROKER_PORT, BROKER_KEEPALIVE)

        client.loop_start()
        send_payload()

    except KeyboardInterrupt:
        # disconnect
        # client.on_disconnect  = on_disconnect
        client.loop_stop()
        client.disconnect()
