
from concurrent.futures import thread
from multiprocessing import Process
from multiprocessing.spawn import freeze_support
import sys
import threading
import time
import concurrent.futures
import random

# class MuThread (threading.Thread):
#     def __init__(self, name, counter):
#         threading.Thread.__init__(self)
#         self.threadID = counter
#         self.name = name
#         self.counter = counter

#     def run(self):
#         print(f"Starting + {self.name} ")
#         print_date(self.name, self.counter)
#         print (f"Exiting + {self.name} ")

# def print_date(threadName, counter):
#     datefields = []
#     today = datetime.date.today()
#     datefields.append(today)
#     print("%s[%d] : %s" % (threadName, counter, datefields[0]))


# thread1 = MuThread("Thread 1", 1)
# thread2 = MuThread("Thread 2", 2)

# thread1.start()
# thread2.start()

# thread1.join()
# thread2.join()
# print ("Exiting the program")



# def thread_func(sleeptime):
#     time.sleep(sleeptime)
#     print("Wake UP!")

# threadd = threading.Thread(target=thread_func, args=(2,))
# threadd.start()
# print("Some text")


# class ThreadClass():
#     def __init__ (self, seconds):
#         self.delay = seconds

#     def __call__ (self):
#         sleep = self.delay
#         print("Wake uppp")

# t2 = ThreadClass(5)
# thread = threading.Thread(target=t2)
# thread_locking = threading.Thread(target=t2)

# thread.start()
# print(thread.is_alive(), thread_locking.is_alive())
# thread_locking.start()
# print("Some stufffff..")
# thread_locking.join()
# print("After alllll...")

#====================================================Locker+=============================================
# lock = threading.RLock()

# def func(locker, delay):
#     timer = time.time()
#     locker.acquire()
#     time.sleep(delay)
#     locker.release()
#     print ("Done", time.time() - timer)

# t1 = threading.Thread(target=func, args=(lock, 2))
# t2 = threading.Thread(target=func, args=(lock, 2))

# t1.start()
# t2.start()
# print("Started")
#========================================================================================================


#=============================================================Semaphore==================================
# def slave (cond, name):
#     cond.acquire()
#     print(name, "Got semaphore")
#     time.sleep(2)
#     cond.release()
#     print(name, "finished")

# pool = threading.Semaphore(2)
# w1 = threading.Thread(target=slave, args=(pool, "first"))
# w2 = threading.Thread(target=slave, args=(pool, "second"))
# w3 = threading.Thread(target=slave, args=(pool, "third"))
# w4 = threading.Thread(target=slave, args=(pool, "fourth"))

# w1.start()
# w2.start()
# w3.start()
# w4.start()

#============================================================================================================


#========================================Thread_sync===================================================
# def master (cond, delay):
#     cond.acquire()
#     print ("Master locked...")
#     time.sleep(delay)
#     cond.notify_all()
#     print("all notified")
#     cond.release()

# def slave(cond, name):
#     print ("Waiting....", name)
#     cond.acquire()
#     print(name, "Got condition")
#     cond.wait()
#     print(name)
#     cond.release()

# c = threading.Condition()
# m = threading.Thread(target=master, args=(c,2))

# w1 = threading.Thread(target=slave, args=(c, "first"))
# w2 = threading.Thread(target=slave, args=(c, "second"))


# w1.start()
# w2.start()
# time.sleep(1)
# m.start()
#================================================================================================================


#============================================Event===============================================================
# e = threading.Event()

# def master(e):
#     time.sleep(1)
#     print ("Set event...")
#     e.set()

# def slave(e,name):
#     print (name, "waiting...")
#     e.wait()
#     print(name, "finished")

# m = threading.Thread(target=master, args=(e, ))

# w2 = threading.Thread(target=slave, args=(e, "second"))
# w1 = threading.Thread(target=slave, args=(e, "first"))

# w1.start()
# w2.start()
# m.start()
#=================================================================================================================

#========================================Barrier===========================================
# counter = 0
# def slave(cond,name):
#     print(name, "Come to barrier")
#     cond.wait()
#     global counter
#     counter +=1
#     print (name, "finished")

# pool = threading.Barrier(3) 
# w1 = threading.Thread(target = slave, args=(pool, "first"))
# w2 = threading.Thread(target = slave, args=(pool, "second"))
# w3 = threading.Thread(target = slave, args=(pool, "third"))

# w1.start()
# w2.start()
# time.sleep(1)
# w3.start()

# w1.join()
# w2.join()
# w3.join()
# print(counter)
#============================================================================================

#======================================Thread_Pool===========================================
# def calculate(name):
#     print (f"start {name}")
#     time.sleep(random.randint(0,3))
#     print(f"{name} finished")
#     return random.randint(0,10)

# arguments = (
#     "Bill",
#      "Jill",
#       "Till",
#        "Sam",
#         "Tom",
#          "John",)

# with concurrent.futures.ThreadPoolExecutor(max_workers=2) as ex:
#     results = list(ex.map(calculate,arguments))

# print (results)
#==============================================================================================

#=================================Download_Files===============================================
# import os
# import urllib.request
# import threading

# class DownloadThread(threading.Thread):

#     def __init__(self, url, name):
#         threading.Thread.__init__(self)
#         self.name = name
#         self.url = url

#     def run(self):
#         handle = urllib.request.urlopen(self.url)
#         fname = os.path.basename(self.url)
#         with open(fname, "wb") as f_handler:
#             chunk = handle.read(1024)
#             if chunk:
#                 f_handler.write(chunk)
#         msg = "%s downloaded %s" % (self.name, self.url)
#         print(msg)

# def main(urls):
#     for item,url in enumerate(urls):
#         name = "Thread %s" % (item+1)
#         thread = DownloadThread(url,name)
#         thread.start()

    
# if __name__ == "__main__":
#     urls =  ["http://www.irs.gov/pub/irs-pdf/f1040.pdf",
#             "http://www.irs.gov/pub/irs-pdf/f1040a.pdf",
#             "http://www.irs.gov/pub/irs-pdf/f1040ez.pdf",
#             "http://www.irs.gov/pub/irs-pdf/f1040es.pdf",
#             "http://www.irs.gov/pub/irs-pdf/f1040sb.pdf"]
#     main(urls)
#=======================================================================================



import asyncio


async def func():
    print("i`m a func")
    await 1


event_loop = asyncio.gather((func(),))
asyncio.run(event_loop())
