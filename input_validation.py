import pyinputplus as pyip

response = pyip.inputNum('Enter your number: ',limit=2 ,default='N/A')
print(response)

my_email = pyip.inputEmail(prompt='Enter your email address: ')

# Blank keyword argument

my_id = pyip.inputNum('Enter your ID number: ', blank=True)

# limit, timeout, default, blank, allowRegexes, blockRegexes keyword arguments

def adds_up_to_ten(numbers):
    numbers_list = list(numbers)
    for i, digit in enumerate(numbers_list):
        numbers_list[i] = int(digit)
    if sum(numbers_list) != 10:
        raise Exception('The digits must add up to 10, not %s' %(sum(numbers_list)))
    return sum(numbers_list)

new_response = pyip.inputCustom(adds_up_to_ten)
print(new_response)




