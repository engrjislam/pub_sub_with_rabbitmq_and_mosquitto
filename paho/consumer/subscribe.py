import paho.mqtt.client as mqtt

# from send import send_influxdb

from config import BROKER_HOST, BROKER_PORT, BROKER_KEEPALIVE, BROKER_USER, BROKER_PASS
from config import TOPIC_TEMPERATURE, TOPIC_HUMIDITY

from util import get_current_time as now
from callbacks import on_log, on_connect, on_disconnect, on_subscribe, on_unsubscribe
from callbacks import on_new_temperature, on_new_humidity


# ------------------------ CALLBACK FUNCTIONS ------------------------ #
def receive_payload(client, userdata, message):
    # funtionality of this fuction can be moved to separate callback function
    # i.e on_new_temperature & on_new_humidity along their predefined topics.

    print(f"[{now()}] -------------- new reading received --------------")

    topic = message.topic
    qos = message.qos
    payload = str(message.payload.decode("utf-8"))
    retain = message.retain

    print(f"[{now()}]  topic =", topic)
    print(f"[{now()}]  qos =", qos)
    print(f"[{now()}]  payload =", payload)
    print(f"[{now()}]  retain =", retain)

    #'''
    if topic == TOPIC_TEMPERATURE:
        measurement = "temperature"

    elif topic == TOPIC_HUMIDITY:
        measurement = "humidity"
    # else:
    #    print("UNKNOWN TOPIC")
    #'''

    # send to influxdb to save
    if topic == TOPIC_TEMPERATURE or topic == TOPIC_HUMIDITY:
        value = float(payload)
        print(f"[{now()}]  sending '{measurement} = {value}' to the database")
        # send_influxdb(value, measurement)
        print(f"[{now()}]  sent successfully")

    print(f"[{now()}] ---------------------- done ----------------------")


# ------------------------------- ENDS ------------------------------- #


if __name__ == "__main__":
    try:
        # Create an MQTT client and attach our routines to it.
        # client              = mqtt.Client(BROKER_ID)
        client = mqtt.Client()

        # built-in callbacks
        client.on_log = on_log
        client.on_connect = on_connect
        # client.on_subscribe = on_subscribe
        client.on_message = receive_payload

        # used-defined callbacks
        # client.message_callback_add(TOPIC_TEMPERATURE, on_new_temperature)
        # client.message_callback_add(TOPIC_HUMIDITY, on_new_humidity)

        client.username_pw_set(BROKER_USER, BROKER_PASS)
        client.connect(BROKER_HOST, BROKER_PORT, BROKER_KEEPALIVE)

        # Process network traffic and dispatch callbacks. This will also handle
        # reconnecting. Check the documentation at
        # https://github.com/eclipse/paho.mqtt.python
        # for information on how to use other loop*() functions
        client.loop_forever()
    except KeyboardInterrupt:
        # disconnect
        # client.on_unsubscribe = on_unsubscribe
        # client.on_disconnect  = on_disconnect
        client.disconnect()
