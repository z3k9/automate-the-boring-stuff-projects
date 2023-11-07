import re

date_regex = re.compile(r'^(0[1-9]|[12][0-9]|3[01])/(0[1-9]|1[0-2])/(1[0-9]{3}|2[0-9]{3})$')

dates = date_regex.findall()
