import pika


HOST = "localhost"
PORT = 5672

EXCHANGE = "amq.topic"
QUEUE = "queue-sensor"
# QUEUE           = 'queue-consumer'

ROOT_KEY = "sensors.dht"
HUMIDITY_KEY = ROOT_KEY + ".humidity"
TEMPERATURE_KEY = ROOT_KEY + ".temperature"


def main():
    headers = {"x-mqtt-publish-qos": 0, "x-mqtt-dup": False}
    properties = pika.BasicProperties(delivery_mode=1, headers=headers)

    try:
        parameters = pika.ConnectionParameters(host=HOST, port=PORT)
        connection = pika.BlockingConnection(parameters)

        # A single channel is enough to get data from routing_key i.e.,
        # humidity & temperature. Therefore, two seperate channels not
        # declared like as producer.
        channel = connection.channel()
        channel.queue_declare(queue=QUEUE)

        # Data will be available through the 'exchange' and the name of
        # the name of the 'queue'. No need to bind both routing_key i.e.,
        # 'humidity' and 'temperature' seperately like as producer. Rather,
        # bind key pattern with * like 'sensors.dht.*'
        channel.queue_bind(exchange=EXCHANGE, queue=QUEUE, routing_key=ROOT_KEY + ".*")

        def callback(ch, method, properties, body):
            print("----------------- start -----------------")
            # print(" [ch]          %r" % ch)
            # print(" [method]      %r" % method)
            print(" [exchange]    %r" % method.exchange)
            print(" [routing_key] %r" % method.routing_key)
            # print(" [properties]  %r" % properties)
            print(" [body]        %r" % body.decode())
            print("----------------- -end- -----------------")

        channel.basic_consume(queue=QUEUE, on_message_callback=callback, auto_ack=True)

        print(" [*] Waiting for messages. To exit press CTRL+C")

        channel.start_consuming()

    except KeyboardInterrupt:
        channel.stop_consuming()


if __name__ == "__main__":
    main()
