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
print(datetime.datetime.fromtimestamp(time.time()))

# You can compare datetime objects with each other using comparison operators to find out which one precedes the other
halloween_2019 = datetime.datetime(2019,10,31,0,0,0)
christmas_2019 = datetime.datetime(2019,12, 31, 0,0,0)

halloween_2019 > christmas_2019
#False

christmas_2019 != halloween_2019
# True


# timedelta datatype represents a duration of time rather than a moment in time
delta = datetime.timedelta(days=11, hours=23, minutes=9, seconds=45)
delta.days

# The delta.total_seconds() will return the duration of the time in seconds alone
delta.total_seconds()

thousand_days = datetime.timedelta(days=1000)
dt + thousand_days

oct_21 = datetime.datetime(2019, 10, 21, 0,0,0)
about_30_years = datetime.timedelta(days=365*30)

oct_21 - about_30_years

# Pausing until a specific date using while loop

while datetime.datetime.now() < datetime.datetime(2023, 12,12):
    time.sleep(1)

# converting datetime objects into strings
# Use the strftime() method to display a datetime object as a string

oct_21.strfrtime('%Y/%m/%d %H:%M:%S')

# converting strings into datetime functions
# use datetime.datetime.strptime() to display a date string as a datetime object
datetime.datetime.strptime('October 21, 2019', '%B %d %Y')



