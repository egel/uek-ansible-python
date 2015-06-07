#!/usr/bin/env python
import pika
import time

credentials = pika.PlainCredentials('guest', 'guest')
cn = pika.BlockingConnection(
  pika.ConnectionParameters('localhost', 5672, '/', credentials)
)
channel = cn.channel()
channel.queue_declare(queue='hello')
print '[*] Waiting for message. To exit press CTRL+C'

def callback(ch, method, properties, body):
  print "[x] Received: %r" %(body,)
  time.sleep(body.count('.'))
  print "Done"
  ch.basic_ack(delivery_tag=method.delivery_tag)

channel.basic_consume(callback,
                      queue='hello',
                      no_ack=False)
channel.start_consuming()
