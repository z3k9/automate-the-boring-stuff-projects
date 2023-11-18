import requests, bs4

res = requests.get('https://nostarch.com/automatestuff2/')

try:
    res.raise_for_status()
except Exception as exc:
    print('something went wrong %s' % (exc))


example_file = open('example.html', 'wb')

for chunk in res.iter_content(100000):
    example_file.write(chunk)

example_file.close()

# the bs4.BeautifulSoup() function needs to be called with a string containing the html it will parse
# the bs4.BeautifulSoup() function returns a beautifulsoup object

example_file = open('example.html')
example_soup = bs4.BeautifulSoup(example_file.read(), 'html.parser')

# The select() method will return a list of tag objects 
elems = example_soup.select('#author')
type(elems)
# <class 'list'>
len(elems)
# 1
type(elems[0])
# <class 'bs4.element.Tag'>
str(elems[0])
# '<span id="author">Al Sweigart<span>'
elems[0].getText()
# 'Al Sweigart'
elems[0].attrs
# {'id':'author'}