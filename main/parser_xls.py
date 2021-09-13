import xlrd

path = "C:/Users/IbragimovaA/Documents/Audit/_reestr_sszi.xls"


def parse(path):
    wb = xlrd.open_workbook(path)
    sh = wb.sheet_by_index(0)
    for rownum in range(sh.nrows):
        print(sh.row_values(rownum))


if __name__ == '__main__':
    parse(path)
