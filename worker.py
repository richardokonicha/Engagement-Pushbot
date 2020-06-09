import os

import redis
from rq import Worker, Queue, Connection

listen = ['high', 'default', 'low']

redisi = "redis://h:pf148522bd570fe8cc658f2b035320b318d584d740875f42f613ce6725077fbd0@ec2-18-200-224-51.eu-west-1.compute.amazonaws.com:16339"

redis_url = os.getenv('REDISTOGO_URL', redisi)

# redis_url = os.getenv('REDISTOGO_URL', 'redis://localhost:6379')

conn = redis.from_url(redis_url)

if __name__ == '__main__':
    with Connection(conn):
        worker = Worker(map(Queue, listen))
        worker.work()