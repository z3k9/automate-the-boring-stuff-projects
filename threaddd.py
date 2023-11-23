import threading, time, datetime

print('Start the program')

def take_a_nap():
    time.sleep(5)
    print('Wake up')

thread_obj = threading.Thread(target=take_a_nap)
thread_obj.start()

print('End of a program')


# Passing arguments to the thread's target function
thread_obj_2 = threading.Thread(target=print, args=['cats', 'dogs', 'frogs'], kwargs={'sep' :' & '})
thread_obj_2.start()


# thread.join()
# The main thread moves on as normal while the other thread works. Calling a thread object's join() method will
# block until that thread has finished


# you can open other programs with python
# you can start other programs in python with Popen() function in the built in subprocess module
# 