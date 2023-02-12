import os


# broker settings
# ---------------
# BROKER_HOST = os.environ.get("BROKER_HOST", "iot.eclipse.org")
# BROKER_HOST = os.environ.get("BROKER_HOST", "test.mosquitto.org")
# BROKER_HOST = os.environ.get("BROKER_HOST", "localhost")
BROKER_HOST = os.environ.get("BROKER_HOST", "127.0.0.1")
# BROKER_HOST      = os.environ.get("BROKER_HOST", "192.168.1.128")
BROKER_PORT = int(os.environ.get("BROKER_PORT", 1883))
BROKER_KEEPALIVE = int(os.environ.get("BROKER_KEEPALIVE", 60))
# BROKER_ID        = os.environ.get("BROKER_ID", "house")
BROKER_USER = os.environ.get("BROKER_USER", "guest")
BROKER_PASS = os.environ.get("BROKER_PASS", "guest")

# topics
# ------
TOPIC_ROOT = "sensors/dht"
TOPIC_TEMPERATURE = TOPIC_ROOT + "/temperature"
TOPIC_HUMIDITY = TOPIC_ROOT + "/humidity"

# sleep time
SLEEP = int(os.environ.get("SLEEP", 5))

# DHT sensor settings
# -------------------
MODEL = int(os.environ.get("MODEL", 22))  # DHT model
PIN = int(os.environ.get("PIN", 23))  # BCM pin

# InfluxDB credentials
DB_HOST = os.environ.get("INFLUXDB_HOST", "localhost")
DB_PORT = os.environ.get("INFLUXDB_PORT", 8086)
DB_USER = os.environ.get("INFLUXDB_USER", "influxDBuser")
DB_PASS = os.environ.get("INFLUXDB_USER_PASSWORD", "influxDBpass")
DB_NAME = os.environ.get("INFLUXDB_DB", "dht")
