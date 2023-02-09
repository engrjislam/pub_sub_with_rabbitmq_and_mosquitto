# pub_sub_with_rabbitmq_and_mosquitto
Pub-Sub with RabbitMQ and Mosquitto Broker. These code were tested under python 3.10.6 (with setuptools 59.6.0 & pip 22.0.2).

## Download Repository
```
git clone git@github.com:engrjislam/pub_sub_with_rabbitmq_and_mosquitto.git
cd pub_sub_with_rabbitmq_and_mosquitto
```

## Python Virtual Environment Setup
This repository requires paho-mqtt (1.6.1) and pika (1.3.1). Let's install in python virtual environment.
```
python3 -m venv vPy3
source vPy3/bin/activate

pip install pika==1.3.1 paho-mqtt==1.6.1
```

## Artificially Data Generation and Consume Those

### Data Generation
Data can be generated either by broker/producer.py or pub/src/publish.py.

#### By producer
```
python broker/producer.py
```

#### By publisher
```
python pub/src/publish.py
```

### Data Consumption
Data can be consumed either by broker/consumer.py or pub/src/subscribe.py.

#### By consumer
Change value of 'QUEUE' to 'mqtt-subscription-sensors-dhtqos0' (otherwise, it is required to run eighter of producer/consumer to run topic/routing_key with the exchange) and run
```
python broker/consumer.py
```
#### By subscriber
Following approach will not grab data from a queue that were used to store data. So earlier data will be discarded (but they will be in the queue).
```
python sub/src/subscribe.py
```
