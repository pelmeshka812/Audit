import json

from pandas_ods_reader import read_ods

path = "C:/Users/IbragimovaA/Documents/Audit/_reestr_sszi.ods"


# load a sheet based on its index (1 based)
# sheet_idx = 1
# df = read_ods(path, sheet_idx)
#
# # load a sheet based on its name
# sheet_name = "sheet1"
# df = read_ods(path, sheet_name)
#
# # load a file that does not contain a header row
# # if no columns are provided, they will be numbered
# df = read_ods(path, 1, headers=False)

# load a file and provide custom column names
# if headers is True (the default), the header row will be overwritten
def excel_parse(path):
    df = read_ods(path, 1, headers=False, columns=["A", "B", "C", "D"])
    # result = df.to_json(orient="split")
    # parsed = json.loads(result)
    # print(json.dumps(parsed, indent=4))
    mylist = list()
    for i in df.columns:
        mylist += map(str, df[i].values.tolist())
    print(mylist)
    return df



if __name__ == '__main__':
    excel_parse(path)
    # f = open('text.txt', 'w')
    # f.write(str(excel_parse(path)))
    # f.close()
