from apscheduler.schedulers.blocking import BlockingScheduler
from apscheduler.schedulers.background import BackgroundScheduler
import time
import datetime
# scheduler = BlockingScheduler()
scheduler = BackgroundScheduler()
knowit = datetime.datetime.now() + datetime.timedelta(seconds=10)
@scheduler.scheduled_job('date', id="hello", run_date=knowit)
def hello():
    print("hello world yess")

# scheduler.add_job(hello, 'interval', seconds=5)
scheduler.start()

print("this is the nezxt")
time.sleep(15)
print('what next')





# from datetime import datetime
# import time
# import os

# from apscheduler.schedulers.background import BackgroundScheduler
# def tick():
#     print('Tick! The time is: %s' % datetime.now())

# if __name__ == '__main__':
#     scheduler = BackgroundScheduler()
#     scheduler.add_job(tick, 'interval', seconds=3)
#     scheduler.start()
#     print('Press Ctrl+{0} to exit'.format('Break' if os.name == 'nt' else 'C'))

#     try:
#         # This is here to simulate application activity (which keeps the main thread alive).
#         while True:
#             time.sleep(2)
#     except (KeyboardInterrupt, SystemExit):
#         # Not strictly necessary if daemonic mode is enabled but should be done if possible
#         scheduler.shutdown()