import re


## Passing a string value representing your regular expression to re.compile() returns a Regex pattern object

phone_regex = re.compile(r'(\d{3})-(\d{3}-\d{4})')

# now the phone_regex variable contains a Regex object
mo = phone_regex.search('My number is 435-987-6789')

area_code, main_num = mo.groups()

print('Phone number found', main_num)
print('The area code is', area_code)

# retrieve all the groups at once 
print(mo.groups())

# Matching mulitple groups with the pipe (|)

hero_regex = re.compile(r'Batman|Tina Fey')
no1 = hero_regex.search('Batman and Tina Fey')
print(no1.group())

# you can find all occcurrences with the findall() method

bat_regex = re.compile(r'Bat(man|mobile|copter|bat)')
mo1 = bat_regex.search('Batmobile lost a wheel')
mo1.group()


# optional matching

bat_woman = re.compile(r'Bat(wo)?man')
mo2 = bat_woman.search('The adventures of batwoman')
mo2.group()


# The * means match 0 or more 

bat_woman = re.compile(r'Bat(wo)*man')
mo3 = bat_woman.search('The adventures of Batwowowowowoman')
mo3.group()


# + to match one or more

bat_woman = re.compile(r'Bat(wo)+man')
mo4 = bat_woman.search('The adventures of Batman')
mo4.group() == None


# The question mark can have 2 meanings in python regex, one for optional matching and for non-greedy matching

# If there are groups in the regular expression then findall() will return a list of tuples

xmas_regex = re.compile(r'\d+\s\w+')
mo5 = xmas_regex.findall('12 drummers, 11 pipers, 10 lords, 9 ladies, 8 maids, 7 swans, 6 geese, 5 rings, 4 birds, 3 hens')
mo5.group()


# ^ - beginning
# $ - end
# . - wildcard character matches any character apart from newline, .* uses greedy mode, use .*? to match in non-greedy mode

# matching new line with .

newline_regex = re.compile(r'.*', re.DOTALL)
mo6 = newline_regex.search('Serve the public trust.\nProtect the innocent.\nUphold the law')


# Case Insensitive matching

robocop = re.compile(r'robocop', re.IGNORECASE)
mo7 = robocop.search('Robocop is part man, part machine, full cop').group()


# Substituting Strings with Sub method

agent_name = re.compile(r'Agent (\w)\w*')
agent_name.sub(r'\1****', 'Agent Alice told Agent Carol that Agent Bob knew that Agent Eve was a double agent')

# Managing complex Regexes using re.verbose to ignore whitespace and comments in the regex string

phone_regex = re.compile(r'''(
    (\d{3}|\(\d{3}\))?
    (\s|-|\.)?
    \d{3}
    (\s|-|\.)?
    \d{4}
    (\s*(ext|x|ext.)\s*\d{2,5})?                   
)''', re.VERBOSE)


# combining re.IGNORECASE, re.VERBOSE, re.DOTALL

some_regex = re.compile(r'foo', re.VERBOSE|re.IGNORECASE|re.DOTALL)



