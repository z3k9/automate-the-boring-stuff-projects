import requests, os, bs4

url = 'https://xkcd.com'
os.makedirs('xkcd', exist_ok=True)

while not url.endswith('#'):
    print('Downloading page %s' % url)
    res = requests.get(url)
    try:
        res.raise_for_status()
    except Exception as exc:
        print('Error encountered %s' %(exc))
    
    soup = bs4.BeautifulSoup(res.text, 'html.parser')
    img_elem = soup.select('#comic img')
    if img_elem == []:
        print('Could not find comic image')
    else:
        img_url = 'https:' + img_elem[0].get('src')

        res = requests.get(img_url)
        try:
            res.raise_for_status()
        except Exception as exc:
            print('Error encountered %s' %(exc))
        image_file = open(os.path.join('xkcd',os.path.basename(img_url)), 'wb')
        
        for chunk in res.iter_content(100000):
            image_file.write(chunk)
        image_file.close()
        
    prev_link = soup.select('a[rel="prev"]')[0]

    url = 'https://xkcd.com'+prev_link.get('href')
