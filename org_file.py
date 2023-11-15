import shutil, os
from pathlib import Path
import send2trash
import zipfile

# calling shutil.copy(source, destination) will copy the file at the path source to the folder at the path destination. This function
# returns a string or Path object of the copied file.

p = Path.home()
shutil.copy(p / 'spam.txt', p / 'some_folder')

# while shutil.copy() will copy a single file, shutil.copytree will copy an entire folder and every folder and file contained in it
# shutil.copytree(source, destination) will copy the folder at the path source, along with all the files and subfolders to the folder at 
# the path destination

shutil.copytree(p / 'spam', p / 'spam_backup')

# Calling shutil.move(source, destination) will move the file or folder at the path source to destination and will return a string of 
# the absolute path of the new location. If destination points to a folder the source file gets moved into destination and keeps its 
# current file name

shutil.move('C:\\bacon.txt', 'C:\\eggs')

# The destination path can also specify a file name
shutil.move('C:\\bacon.txt', 'C:\\eggs\\new_bacon.txt')


# Permanently deleting files and folders
# You can delete a single file or an empty folder with functions in the os module, whereas to delete a folder and all its contents you use the shutil module

os.unlink(path) # delete the file at path
os.rmdir(path) # delete the folder at path. Folder must be empty

shutil.rmtree(path) # delete the folder at path with all files and folders

# Using send2trash to safely delete files
bacon_file = open('bacon.txt', 'a')
bacon_file.write('Bacon is not a vegetable')
bacon_file.close()

send2trash.send2trash('bacon.txt')


# Walking a directory tree
for folder_name, subfolders, filenames in os.walk():
    print('The current folder is '+ folder_name)

    for subfolder in subfolders:
        print('Subfolder of ' + folder_name + ':' + subfolder)

    for filename in filenames:
        print('FILE INSIDE' + folder_name + ':' + filename)
    
    print('')

# since os.walk() returns a list of strings for the subfolder and filename variables we can use these lists in for loops

# Compressing files with the Zipfile module
# A zipfile object has namelist() method that returns a list of strings for all the files and folders contained in the zipfile


example_zip =  zipfile.ZipFile(p / 'example.zip')
example_zip.namelist()
spam_info = example_zip.getinfo('spam.txt')
spam_info.file_size()
spam_info.compress_size()

print(f"Compressed file is {round(spam_info.file_size/spam_info.compress_size, 2)}x smaller!")
example_zip.close()

# Extract from zip files
# The extractall() extracts all the files and folders from a ZIP file into the current working directory
# optionally we can pass a folder name to extractall() to have it extract all the files into a folder other than the cwd

example_zip.extractall()
example_zip.close()

# The extract() method will extract a single file from the specified zip file
# optionally you can pass a second argument to extract() to extract the file into a folder other than the CWD

example_zip.extract('spam.txt')

# Creating and adding to ZIP files
new_zip = zipfile('new.zip', 'w')
new_zip.write('spam.txt', compress_type=zipfile.ZIP_DEFLATED)
new_zip.close()


