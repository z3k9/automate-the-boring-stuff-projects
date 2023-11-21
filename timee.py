import time, datetime

print(time.ctime())

def calc_prod():
    product =1
    for i in range(1, 10000):
        product = product * i
    return product

start_time = time.time()
prod = calc_prod()
end_time = time.time()

print('The result is %s digits long' % (len(str(prod))))
print('This function took %s seconds' % (end_time - start_time))

# The time.ctime returns a string description of the current time

# The time.sleep() - If you need to pause your program for a while

for i in range(4):
    print('Tick')
    time.sleep(2)
    print('Tock')
    time.sleep(2)


# Rounding numbers
now = time.time()

round(now, 2)


# To display dates in a more convenient manner or do arithmetic with dates use datetime module

datetime.datetime.now()
# datetime.datetime(2023, 11, 21, 15, 38, 53, 386205)

dt = datetime.datetime(2019, 10, 11, 16, 30, 0)
print(dt.year, dt.month, dt.day)
print(dt.hour, dt.minute, dt.second)

# a unix timestamp can be converted into a datetime object with the datetime.datetime.fromtimestamp()
