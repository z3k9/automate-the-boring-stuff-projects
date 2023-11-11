from pathlib import Path
import os
import shelve
import pprint

Path('spam', 'bacon', 'eggs')
str(Path('spam', 'bacon', 'eggs'))

# Present working directory
Path.cwd()

# Change directory
os.chdir('Path to directory')


# Home directory
Path.home()

# create new folders 
os.makedirs('C:\\delicious\\walnut\\waffles')

Path(r'C:\Users\Al\Spam').mkdir()

# mkdir() can only make one dir at a time it won't make several subdirectories like os.makedirs()

# The Path lib has mehods for checking if a path is the absolute path and for returning the absolute path of a relative path

Path.cwd()

Path.cwd().is_absolute()

# to get an absolute path from a relative path 
Path.cwd() / Path('my/relative/path')

# To return the string of the absolute path
os.path.abspath(path)

# To return if the path is an absolute path or relative path
os.path.isabs(path)

# to return a string of the relative path from the start path to path
os.path.relpath(path, start)


# p.anchor, p.parent, p.name, p.stem, p.suffix, p.drive

# the parents attribute (different from parent) evaluates to the ancestor folders of a Path object with an integer index

# os.path() has similar functions for getting the different parts of a path written in a string

os.path.dirname(path) # returns a string of everything before the last slash
os.path.basename(path) # returns a string of everything after the last slash

# if you need a path's dir name and base name together = os.path.split() to get a tuple value of the 2 strings
# The os.path.split() does not take a filepath and return a list of strings. 

calc_filepath = 'C:\\Windows\\System32\\calc.exe'

calc_filepath.split(os.sep) # This returns all the paths of the path as strings


# Finding file sizes and folder content
os.path.getsize(path) # finding file sizes in bytes
os.listdir(path) # folder content

# glob() is simpler to use than listdir()

p = Path('C:/Users/Al/Desktop')
p.glob('*')
list(p.glob('*'))

# Checking path validity
p.exists() # returns True if the path exists or returns False if it doesn't
os.path.exists()

p.is_file() # returns True if the path exists and is a file, returns False instead
os.path.isfile()

p.is_dir() # returns True if the path exists and is a dir, returns False instead
os.path.isdir()

spam_doc = Path('spam.txt')
spam_doc.write_text('Hello, World')
spam_doc.read_text()

# Opening files with open()
hello_file = open(Path.cwd() / 'hello_file.txt');

# Reading from open file
hello_file.read()

# To get a list of string values from the line
hello_file.readlines()

# Write to a file
new_doc = ('new_doc.txt', 'w') # new_doc = ('new_doc.txt', 'a') open in append mode if you want to add to an existing file
inp = hello_file.read()
new_doc.write(inp)
new_doc.close()

# Saving variables with the shelve module. Save variables in python program to binary shelf files

shelf_file = shelve.open('mydata')
cats = ['zophie', 'pooka', 'simon']
shelf_file['cats'] = cats
shelf_file.close()

# retrieving data stored in a shelve
shelf_file = shelve.open('mydata')
shelf_file['cats']

# Saving variables with pprint.pformat()
dogs = [{'name': 'Rats', 'desc':'skinny'}, {'name':'brad', 'desc': 'fluffy'}]
pprint.pformat(dogs)
file_obj = open('my_dogs.py', 'w')
file_obj.write('cats = ' + pprint.pformat(dogs) + '\n')
file_obj.close()
