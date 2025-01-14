import pika
import pymongo
import json

RABBITMQ_HOST = 'rabbitmq'
MONGO_URI = 'mongodb://mongo1:27017'

connection = pika.BlockingConnection(pika.ConnectionParameters(host=RABBITMQ_HOST))
channel = connection.channel()
channel.queue_declare(queue='AAPL')

client = pymongo.MongoClient(MONGO_URI)
db = client.stockmarket
collection = db.stocks

def callback(ch, method, properties, body):
    data = json.loads(body)
    print(f"Received {data}")
    collection.insert_one(data)

channel.basic_consume(queue='AAPL', on_message_callback=callback, auto_ack=True)
print('Waiting for messages...')
channel.start_consuming()
