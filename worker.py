
# background process
import os
import redis
from rq import Queue, Worker, Connection

listen = ["high", "default", "low"]

redisi = "redis://h:pf148522bd570fe8cc658f2b035320b318d584d740875f42f613ce6725077fbd0@ec2-18-200-224-51.eu-west-1.compute.amazonaws.com:16339"

redis_url = os.getenv('REDIS_URL', redisi)

# conn = redis.from_url(redis_url)

conn = redis.Redis(
    host='redis-13324.c89.us-east-1-3.ec2.cloud.redislabs.com', 
    port=13324, 
    password="konichar"
    )

print("redis url set", conn)

if __name__ == "__main__":
    with Connection(conn):
        worker = Worker(map(Queue, listen))
        worker.work()
