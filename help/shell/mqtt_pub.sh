# help:
# -----
# http://www.steves-internet-guide.com/mosquitto_pub-sub-clients/
# mosquitto_pub --help

# MQTT publish:
# sends data to MQTT subscriber
# ---------------------------------
mosquitto_pub -h 192.168.1.128 -p 1883 -t sensors/dht/temperature -m 22.5 -d
