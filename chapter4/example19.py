# consumer.py

import pika

QUEUE_NAME = 'scrape1'
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()
# channel.queue_declare(queue=QUEUE_NAME)

# def callback(ch, method, properties, body):
#     print(f"Get {body}")

# channel.basic_consume(queue='scrape',
#                         auto_ack=True,
#                         on_message_callback=callback)
# channel.start_consuming()

while True:
    input()
    method_frame, header, body = channel.basic_get(
        queue=QUEUE_NAME, auto_ack=True
    )
    if body:
        print(f'Get {body}')
