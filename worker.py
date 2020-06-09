
# background process
import os
import redis
from rq import Queue, Worker, Connection

listen = ["high", "default", "low"]

redis_url = os.getenv('REDISTOGO_URL', 'redis://127.0.0.1:6379')

conn = redis.from_url(redis_url)

if __name__=="__main__":
    with Connection(conn):
        worker = Worker(map(Queue, listen))
        worker.work()