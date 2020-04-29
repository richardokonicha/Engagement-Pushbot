import threading
from time import sleep
import time
import sched
import datetime


class RepeatedTimer(object):
    def __init__(self, interval, function,name, *args, **kwargs):
        self._timer = None
        self.interval = interval
        self.function = function
        self.args = args
        self.kwargs = kwargs
        self.is_running = False
        self.next_call = time.time()
        self.name = name
        self.start()

    def _run(self):
        self.is_running = False
        self.start()
        self.function(*self.args, **self.kwargs)

    def start(self):
        if not self.is_running:
            self.next_call += self.interval
            self._timer = threading.Timer(self.next_call - time.time(), self._run)
            self._timer.name = self.name
            self._timer.start()
            self.is_running = True

    def stop(self):
        self._timer.cancel()
        self.is_running = False


# def hello():
#     print("Hello %s!")


def call_me():
    u = True
    while u:
        time.sleep(2)

        print("from thread new thread", i)
        if i == 2:
            u = False
    print("free")
    print(threading.current_thread())

# T = datetime.timedelta(seconds=5)


# print("starting...")
# rt = RepeatedTimer(T.total_seconds(), call_me) # it auto-starts, no need of rt.start()
# # try:
# #     sleep(1)
# #     print("kjfskjdlfjls") # your long-running job goes here...
# #     sleep(3)
# #     print("kjfskjdlfjls") # your long-running job goes here...
# #     print(2)
# #     print("kjfskjdlfjls") # your long-running job goes here...

# # finally:
# #     rt.stop() # better in a try/finally block to make sure the program ends!

import threading
#%%
import threading
g = threading.Timer(1, call_me)
print(g.getName)
g.name= "sync_thread"
g.start()
print("life is good but come first")

print("life is good")
for i in range(20):
    time.sleep(2)
    print("from main thread ", i)



# %%
