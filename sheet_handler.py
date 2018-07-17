import openpyxl

CELL_SIZE = 50

def create_header(wb):
    t_font = openpyxl.styles.Font(name='Times New Roman', bold=True)

    #Set header
    sheet = wb.active
    sheet.cell(1, 1).value = 'Title'
    sheet.cell(1, 1).font = t_font
    sheet.cell(1, 2).value = 'Cover'
    sheet.cell(1, 2).font = t_font
    sheet.cell(1, 3).value = 'Sample'
    sheet.cell(1, 3).font = t_font
    
    #Adjust cell size
    sheet.column_dimensions['C'].width = CELL_SIZE
    sheet.column_dimensions['C'].height = CELL_SIZE

def insert_title(titles, wb):
    sheet = wb.active

    for idx, titles in enumerate(titles):
        sheet.cell(idx+2, 1).value = titles

def insert_cover_img(wb, img_name, work_num):
    sheet = wb.active
    img = openpyxl.drawing.image.Image(img_name)
    sheet.add_image(img, 'C'+work_num+2)

    img.width = CELL_SIZE
    img.height = CELL_SIZE
    

def test():
    wb = openpyxl.Workbook()

    create_header(wb)

    titles = ['aa', 'bb', 'cc']
    insert_title(titles, wb)

    insert_img(wb)

    wb.save('sheet.xlsx')

if __name__ == '__main__':
    test()