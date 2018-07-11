import requests, os
from bs4 import BeautifulSoup

CHUNK_SIZE = 1000000
PIC_DIR = 'pics'

cookies = {
    'cklg': 'ja',
}

def get_soup_local(url):
    soup = BeautifulSoup(open(url, 'r', encoding="utf-8"), 'html5lib')
    return soup

def get_soup(url):
    resp = requests.get(url, cookies=cookies)
    resp.raise_for_status()
    soup = BeautifulSoup(resp.text, 'html5lib')
    return soup


def get_pop_works(soup):
    works = soup.find_all('div', 'd-modtmb')
    print(works)
    #TODO get href and move to the page -> craw data
"""     for work in works:
        print(work.a['href'])
        w_soup = get_soup(work.a['href'])
        img_url = soup.find('img', {'class': 'tdmm'})
        print(img_url)
        break """


def get_img(img_url):
    os.makedirs(PIC_DIR, exist_ok=True)

    resp = requests.get(img_url)
    resp.raise_for_status()

    file_name = os.path.basename(img_url)
    with open(os.path.join(PIC_DIR, file_name), 'wb') as f:
        print("Saving img '{}' ...".format(file_name))
        for chunck in resp.iter_content(CHUNK_SIZE):
            f.write(chunck)

def test():
    url = 'http://www.dmm.co.jp/digital/videoc/'
    soup = get_soup(url)
    get_pop_works(soup)



    
if __name__ == '__main__':
    test()