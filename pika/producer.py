import pika
import time
import random


HOST = "localhost"
PORT = 5672

EXCHANGE = "amq.topic"
QUEUE = "queue-sensor"
# QUEUE           = 'queue-producer'

ROOT_KEY = "sensors.dht"
HUMIDITY_KEY = ROOT_KEY + ".humidity"
TEMPERATURE_KEY = ROOT_KEY + ".temperature"


def main():
    print("[x] program started! Press 'Ctrl+C' to stop it.")

    headers = {"x-mqtt-publish-qos": 0, "x-mqtt-dup": False}
    properties = pika.BasicProperties(delivery_mode=1, headers=headers)

    try:
        parameters = pika.ConnectionParameters(host=HOST, port=PORT)
        connection = pika.BlockingConnection(parameters)

        channel = connection.channel()
        # channel1 = connection.channel()
        # channel2 = connection.channel()

        channel.queue_declare(queue=QUEUE)
        # channel1.queue_declare(queue=QUEUE)
        # channel2.queue_declare(queue=QUEUE)

        channel.queue_bind(exchange=EXCHANGE, queue=QUEUE, routing_key=ROOT_KEY + ".*")

        # Queue must bind with 'routing_keys' for each MQTT topic (i.e., routing_key)
        # otherwise queue will bind with 'queue name' rather than 'routing_key'.
        # A channel can bind a queue with 'routing_key'. Therefore, 2 channels are
        # needed to bind 'humidity' and 'temperature'.

        # channel1.queue_bind(exchange=EXCHANGE, queue=QUEUE, routing_key=HUMIDITY_KEY)
        # channel2.queue_bind(exchange=EXCHANGE, queue=QUEUE, routing_key=TEMPERATURE_KEY)

        # It is asumed that, both humidty and teperature
        # will be sent in pair and program wait for SLEEP
        # seconds i.e., 5s before sending next pair.
        #
        # First, humidity will then temperature. The program
        # will sleep once temperature is sent.
        # ---------------------------------------------------
        # For the first reading in this pair i.e., 'humidity'
        # , programs does not require to sleep. Hence, the
        # 'isSleepRequired' variable is set to False.
        # ---------------------------------------------------
        isSleepRequired = False

        while True:
            # ------------------------------------------
            # humidity ranges    --> 35.0% Hg ~ 45.0% Hg
            # temperature ranges --> 25.0 *C  ~ 35.0  *C
            # ------------------------------------------
            if isSleepRequired:
                # temperature
                SLEEP = 5
                temperature = random.uniform(25.00, 35.00)
                data = round(temperature, 1)
                routing_key = TEMPERATURE_KEY
                """
                channel1.basic_publish(
                    exchange = EXCHANGE,
                    routing_key = routing_key, 
                    properties = properties, 
                    body = str(data)
                )
                """

            else:
                # humidity
                SLEEP = 0
                humidity = random.uniform(35.00, 45.00)
                data = round(humidity, 1)
                routing_key = HUMIDITY_KEY
                """
                channel2.basic_publish(
                    exchange = EXCHANGE,
                    routing_key = routing_key,
                    properties = properties,
                    body = str(data)
                )
                """
            #'''
            channel.basic_publish(
                exchange=EXCHANGE,
                routing_key=routing_key,
                properties=properties,
                body=str(data),
            )
            #'''

            print("-------------------------- new reading --------------------------")
            print(f" routing_key = {routing_key}")
            print(f" data        = {data}")
            print("-------------------------- xxx xxxxxxx --------------------------")

            time.sleep(SLEEP)
            isSleepRequired = not isSleepRequired

    except KeyboardInterrupt:
        connection.close()


if __name__ == "__main__":
    main()
