import dmm_crawler

soup = dmm_crawler.get_soup(dmm_crawler.DMM_URL)
titles = dmm_crawler.get_pop_works(soup)