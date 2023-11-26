import threading, time, datetime, subprocess

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
# if you want to start an external program from your python script, pass the program's filename to subprocess.Popen()
# Keep in mind that the launched program is not run in the same thread as your python program
# The return value is a Popen() object which has 2 useful methods: poll() and wait()
# poll() will return None if the process is still running at the time poll() is called
# If the program has terminated it will return the process's integer exit code.
# The wait() method will block until the launched program has terminated.

application_name ='TextEdit'

process = subprocess.Popen(['open', '-a', application_name])

process.poll() == None # True
process.wait() # Doesn't return until TextEdit is closed
process.poll() != None # True

# You can run a python script from python by simply passing the python executable to Popen and the filename of the .py script
subprocess.Popen(['/Library/Framework/Python.framework/Versions/3.8/bin/python3', 'hello.py'])