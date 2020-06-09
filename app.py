from rq import Queue

from worker import conn

q = Queue(connection=conn)

from utili import count_words_at_url

result = q.enqueue(count_words_at_url, 'example.url')

print("A non blocking blocker came the block with a wood brooker bruok")