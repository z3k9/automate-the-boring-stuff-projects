import shutil, os, re

date_pattern = re.compile(r"""
    ^(.*?)
    ((0|1)?\d)-
    ((0|1|2|3)?\d)-
    ((19|20)?\d\d)                     
    ^(.*?)$                         
""", re.VERBOSE)

for file_name in os.listdir('.'):
    mo = date_pattern.search(file_name)
    if mo == None:
        continue
    
    before_part = mo.group(1)
    month = mo.group(2)
    day = mo.group(4)
    year = mo.group(6)
    after_part = mo.group(8)

    euro_filename = before_part+ day+ '-'+ month+'-'+year+after_part
    abs_dir = os.path.abspath('.')
    file_name = os.path.join(abs_dir, file_name)
    euro_filename = os.path.join(abs_dir, euro_filename)

    shutil.move(file_name, euro_filename)