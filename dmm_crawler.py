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

#Return poplular work names, and download cover image and sample image
def get_pop_works(soup):
    titles = []
    works = soup.find_all('div', 'd-modtmb')
    for work in works:
        w_url = DMM_URL + work.a['href'].split('/digital/videoc/')[-1]
        print('Work url: {}'.format(w_url))
        w_soup = get_soup(w_url)

        #Get title
        #title = w_soup.find('h1', {'id': 'title'}).text
        title = os.path.basename(os.path.dirname(w_soup.find('img', {'class': 'tdmm'})['src']))
        titles.append(title)
        print('Title: {}'.format(title))
        work_dir = os.path.join(PIC_DIR, title)

        #Get cover img
        cover_img_url = w_soup.find('img', {'class': 'tdmm'})['src']
        cover_dir = os.path.join(work_dir, 'cover')
        get_img(cover_img_url, cover_dir)

        #Get sample img
        sample_img_url = [ u['src'] for u in w_soup.find_all('img', {'class': 'mg-b6'})]
        sample_dir = os.path.join(work_dir, 'sample')
        for s_img_url in sample_img_url: get_img(s_img_url, sample_dir)

        break
    
    return title


def get_img(img_url, folder_dir):
    os.makedirs(folder_dir, exist_ok=True)

    resp = requests.get(img_url)
    resp.raise_for_status()

    file_name = os.path.basename(img_url)
    with open(os.path.join(folder_dir, file_name), 'wb') as f:
        print("Saving img '{}' ...".format(file_name))
        for chunck in resp.iter_content(CHUNK_SIZE):
            f.write(chunck)

def test():
    soup = get_soup(DMM_URL)
    get_pop_works(soup)



    
if __name__ == '__main__':
    test()