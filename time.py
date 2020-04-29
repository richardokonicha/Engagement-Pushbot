# #%%
# import sched
# import time
# import datetime

# ti = time.time

# s = sched.scheduler(time.time, time.sleep)
# def print_time(a='default'):
#     print("From print_time", time.time(), a)

# def print_some_times():
#      print(time.time())
#      s.enter(10, 1, print_time)
#      s.enter(5, 2, print_time, argument=('positional',))
#      s.enter(5, 1, print_time, kwargs={'a': 'keyword'})
#      s.run(blocking=False)
#      print(time.time())


# # datetime.datetime.fromtimestamp(time.time()).timestamp()
# # datetime.datetime.now().timestamp()

# print_some_times()

# print("hjdskjfdkjfjk")

# time.sleep(5)
# # %%


# # when round starts

# # user clicks button to join round

# # when round ends drop session becomes false and roound starts

# # sends list of a participants to all participants

from epush_bot import update_round
update_round()