import requests, os
from bs4 import BeautifulSoup

DMM_URL = 'http://www.dmm.co.jp/digital/videoc/'
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
    for work in works:
        w_url = DMM_URL + work.a['href'].split('/digital/videoc/')[-1]
        print(w_url)
        w_soup = get_soup(w_url)

        #Get cover img
        cover_img_url = w_soup.find('img', {'class': 'tdmm'})['src']
        print(cover_img_url)
        #get_img(cover_img_url)

        #Get sample img
        sample_img_url = [ u['src'] for u in w_soup.find_all('img', {'class': 'mg-b6'})]
        print(sample_img_url)
        for s_img_url in sample_img_url: get_img(s_img_url)

        break


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
    soup = get_soup(DMM_URL)
    get_pop_works(soup)



    
if __name__ == '__main__':
    test()