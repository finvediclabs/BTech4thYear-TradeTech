class KafkaClient:
    def __init__(self, bootstrap_servers):
        from kafka import KafkaProducer, KafkaConsumer
        self.producer = KafkaProducer(bootstrap_servers=bootstrap_servers)
        self.consumer = KafkaConsumer(bootstrap_servers=bootstrap_servers)

    def send_message(self, topic, message):
        self.producer.send(topic, value=message.encode('utf-8'))
        self.producer.flush()

    def receive_messages(self, topic):
        self.consumer.subscribe([topic])
        for message in self.consumer:
            yield message.value.decode('utf-8')