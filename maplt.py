import webbrowser, sys, pyperclip
import requests

if len(sys.argv) > 1:
    address = ' '.join(sys.argv[1:])
else:
    address = pyperclip.paste()

webbrowser.open('https://www.google.com/maps/place/' + address)


res = requests.get('https://automateboringstuff.com/files/rj.txt')
print(type(res))


try:
    res.raise_for_status()
except Exception as exc:
    print('There was a problem %s' %(exc))


res.status_code == requests.codes.ok

# The raise_for_status() method is good way to ensure that the program halts if a bad download occurs.
# Always call raise_for_status() after calling requests.get()


# Saving downloaded files to the harddrive
play_file = open('RomeoandJuliet.txt', 'wb')
for chunk in res.iter_content(100000):
    play_file.write(chunk)
play_file.close()

# the iter_content() returns chunks of the content on each iteration through the loop
# The write() method returns the number of bytes written to a file


