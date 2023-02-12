import os


BROKER_HOST = os.environ.get("BROKER_HOST", "shostakovich")
BROKER_PORT = int(os.environ.get("BROKER_PORT", 1883))
BROKER_KEEPALIVE = int(os.environ.get("BROKER_KEEPALIVE", 60))
BROKER_USER = os.environ.get("BROKER_USER", "guest")
BROKER_PASS = os.environ.get("BROKER_PASS", "guest")

TOPIC_ROOT = "sensors/dht"
TOPIC_TEMPERATURE = TOPIC_ROOT + "/temperature"
TOPIC_HUMIDITY = TOPIC_ROOT + "/humidity"

SLEEP = int(os.environ.get("SLEEP", 5))

MODEL = int(os.environ.get("MODEL", 22))
PIN = int(os.environ.get("PIN", 23))
