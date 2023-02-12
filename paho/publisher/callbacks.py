from config import TOPIC_TEMPERATURE, TOPIC_HUMIDITY

from util import get_current_time as now


# -------------------------- built-ins -------------------------- #
def on_log(client, userdata, level, buf):
    print(f"[{now()}]", buf)

def on_connect(client, userdata, flags, rc):
    print(f"[{now()}] Connected with result code " + str(rc))
 
    # Subscribing in on_connect() - if we lose the connection and
    # reconnect then subscriptions will be renewed.
    # qos -> 0, 1, 2; default vlaue for qos is 0
    #client.subscribe(TOPIC_TEMPERATURE)                                # without qos
    #client.subscribe((TOPIC_HUMIDITY, 0))                              # with qos
    #client.subscribe([TOPIC_TEMPERATURE, TOPIC_HUMIDITY])              # list
    client.subscribe([(TOPIC_TEMPERATURE, 0), (TOPIC_HUMIDITY, 0)])    # tuples list

def on_subscribe(client, userdata, mid, granted_qos):
	# pass
	print(f"[{now()}] Subscribing ... ")

def on_unsubscribe(client, userdata, mid):
	# pass
	print(f"[{now()}] Unsubscribing ... ")

def on_disconnect(client, userdata, rc):
    print(f"[{now()}] Disconnecting ...")

    # Subscribing in on_connect() - if we lose the connection and
    # reconnect then subscriptions will be renewed.
    client.unsubscribe(TOPIC_TEMPERATURE)
    client.unsubscribe(TOPIC_HUMIDITY)

    print(f"[{now()}] Disconnected with result code " + str(rc))

def on_publish(client, userdata, mid):
    # pass
    print(f"[{now()}] Publishing ... ")
# ------------------------xx built-ins xx------------------------ #


# ------------------------- user-defined ------------------------- #
def on_new_temperature(client, userdata, message):
    #pass
    #print()
    print(f"[{now()}] -------------- new reading received --------------")
    
    topic = message.topic
    qos = message.qos
    payload = str(message.payload.decode("utf-8"))
    retain = message.retain
    
    print(f"[{now()}]  topic =", topic)
    print(f"[{now()}]  qos =", qos)
    print(f"[{now()}]  payload =", payload)
    print(f"[{now()}]  retain =", retain)
    
    #print("NEW TEMPERATURE READING FOUND FROM DHT22 SENSOR")
    temperature = float(payload)
    print(f"[{now()}]  Temperature = %.1f *C" % temperature)
    
    # send to influxdb to save
    print(f"[{now()}]  Data is sending to save into database")
    #send_influxdb(temperature)
    print(f"[{now()}]  Saved successfully")
    
    print(f"[{now()}] ---------------------- done ----------------------")
    print()
	
def on_new_humidity(client, userdata, message):
    print(f"[{now()}] -------------- new reading received --------------")
    
    topic = message.topic
    qos = message.qos
    payload = str(message.payload.decode("utf-8"))
    retain = message.retain
    
    print(f"[{now()}]  topic =", topic)
    print(f"[{now()}]  qos =", qos)
    print(f"[{now()}]  payload =", payload)
    print(f"[{now()}]  retain =", retain)
    
    #print("NEW HUMIDITY READING FOUND FROM DHT22 SENSOR")
    humidity = float(payload)
    print(f"[{now()}]  Humidity    = %.1f %%" % humidity)
    
    # send to influxdb to save
    print(f"[{now()}]  Data is sending to save into database")
    #send_influxdb(humidity, measurement='humidity')
    print(f"[{now()}]  Saved successfully")
    
    print(f"[{now()}] ---------------------- done ----------------------")
# -----------------------xx user-defined xx----------------------- #