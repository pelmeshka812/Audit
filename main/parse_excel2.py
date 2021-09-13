from pyexcel_ods import get_data
import json

path = "C:/Users/IbragimovaA/Documents/Audit/_reestr_sszi.ods"


def parse(path):
    data = get_data(path, start_row=1, row_limit=4)
    print(data)


if __name__ == '__main__':
    parse(path)
