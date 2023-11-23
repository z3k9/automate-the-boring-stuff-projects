import requests, os, bs4, time, threading

url = 'https://xkcd.com'
os.makedirs('xkcd', exist_ok=True)

def download_xkcd(start_comic, end_comic):

    for url_num in range(start_comic, end_comic):
        print('Downloading the page https://xkcd.com/%s...' % (url_num))
        res = requests.get('https://xkcd.com/%s' % (url_num))
        res.raise_for_status()

        soup = bs4.BeautifulSoup(res.text, 'html.parser')
        comic_elem = soup.select('#comic img')
        if comic_elem == []:
            print('could not find comic image')
        else:
            comic_url = comic_elem[0].get('src')
            res = requests.get('https:'+ comic_url)
            res.raise_for_status()
            image_file = open(os.path.join('xkcd', os.path.basename(comic_url)), 'wb')

            for chunk in res.iter_content(100000):
                image_file.write(chunk)
            image_file.close()


download_threads = []
for i in range(0 ,140, 10):
    start = i
    end = i + 9
    if start == 0:
        start = 1
    download_thread = threading.Thread(target=download_xkcd, args=(start , end))
    download_threads.append(download_thread)
    download_thread.start()

for download_thread in download_threads:
    download_thread.join()
print('Done')
