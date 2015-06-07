#!/usr/bin/env python
import pika
import sys

credentials = pika.PlainCredentials('guest', 'guest')
cn = pika.BlockingConnection(
  pika.ConnectionParameters('localhost', 5672, '/', credentials)
)
channel = cn.channel()
channel.queue_declare(queue='hello')

msg = ' '.join(sys.argv[1:])

channel.basic_publish(
  exchange='',
  routing_key='hello',
  body=msg
)

cn.close() # connection close
