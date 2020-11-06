import xlrd


def read_xls(path):
    xl = xlrd.open_workbook(path)
    sheet = xl.sheets()[0]  # 0表示读取第一个工作表sheet
    data = []
    for i in range(0, sheet.ncols):  # ncols表示按列读取
        data.append(list(sheet.col_values(i)))
    return data


path = r'S:\Desktop\QQFile\灯泡网盘软件网站合集.xlsx'
print(read_xls(path))
# xlrd为第三方包，可以通过用pip下载，具体操作：打开运行，输入cmd→在cmd中输入pip install xlrd，enter →等待安装完成即可。在后续若存在需要使用的第三方包，都可以通过这种方式下载和安装。
# 传入参数为path，path为excel所在路径。
# 传入的path需如下定义：path= r’ D:\excel.xlsx’或path= r’ D:\excel.xls’
# col_values(i)表示按照一列中的所有单元格遍历读取
# 可以根据需求，把col替换成row，则表示按行读取
# return data ：返回的data是一个二维数组，根据col和row，传回的数据呈现形式也不同，即row是col的转置。
