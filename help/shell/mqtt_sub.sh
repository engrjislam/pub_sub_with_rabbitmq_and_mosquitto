# help:
# -----
# http://www.steves-internet-guide.com/mosquitto_pub-sub-clients/
# mosquitto_sub --help

# MQTT sbuscribe: 
# receives data from MQTT publisher
# ---------------------------------
mosquitto_sub -h 192.168.1.128 -p 1883 -t sensors/dht/temperature -v -C 10 -d
#mosquitto_sub -h 192.168.1.128 -p 1883 -t sensors/dht/humidity -v -C 10 -d
