import openpyxl

def create_header(wb):
    t_font = openpyxl.styles.Font(name='Times New Roman', bold=True)

    sheet = wb.active
    sheet.cell(1, 1).value = 'Title'
    sheet.cell(1, 1).font = t_font
    sheet.cell(1, 2).value = 'Cover'
    sheet.cell(1, 2).font = t_font
    sheet.cell(1, 3).value = 'Sample'
    sheet.cell(1, 3).font = t_font

def insert_title(titles, wb):
    sheet = wb.active

    for idx, titles in enumerate(titles):
        sheet.cell(idx+2, 1).value = titles

def insert_img(wb):
    sheet = wb.active
    img = openpyxl.drawing.image.Image('logo.png')
    img.width = 50
    img.height = 50
    sheet.add_image(img, 'E5')

def test():
    wb = openpyxl.Workbook()

    create_header(wb)

    titles = ['aa', 'bb', 'cc']
    insert_title(titles, wb)

    insert_img(wb)

    wb.save('sheet.xlsx')

if __name__ == '__main__':
    test()