import webbrowser,sys, requests, bs4


res = requests.get('https://www.pypi.org/search?q=' + ' '.join(sys.argv[1:]))

try:
    res.raise_for_status()
except Exception as exc:
    print('Could not load page %s' % (exc))

soup = bs4.BeautifulSoup(res.text, 'html.parser')

link_elems = soup.select('.package-snippet')

num_open = min(5, len(link_elems))


for result in range(num_open):
    url_to_open = 'https://www.pypi.org' + link_elems[result].get('href')
    webbrowser.open(url_to_open)
    print('Opening', url_to_open)


print(sys.argv[1:])
