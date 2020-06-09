
# background process
import os
import redis
from rq import Queue, Worker, Connection

listen = ["high", "default", "low"]

redis_url = os.getenv('REDIS_URL', 'redis://127.0.0.1:6379')

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
