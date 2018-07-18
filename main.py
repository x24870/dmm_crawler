import os, openpyxl
import dmm_crawler, sheet_handler

#Get work images
soup = dmm_crawler.get_soup(dmm_crawler.DMM_URL)
works = dmm_crawler.get_pop_works(soup)
print('Total works: {}'.format(len(works)))

#Create .xlsx file
wb = openpyxl.Workbook()
sheet_handler.create_header(wb)

works = os.listdir(dmm_crawler.PIC_DIR)
for idx, work in enumerate(works):
    sheet_handler.insert_title(wb, work, idx)
    sheet_handler.insert_cover_img(wb, work, idx)
    sheet_handler.insert_sample_img(wb, work, idx)

wb.save('sheet.xlsx')