import os


def getdirsize(dir):
    size = 0
    for root, dirs, files in os.walk(dir):
        size += sum([os.path.getsize(os.path.join(root, name)) for name in files])
    return size

def scondkey(elem):
    return elem[1]

if __name__ == '__main__':
    listdirs = os.listdir('D:/')
    list1 = []
    for i in listdirs:
        list2 = []
        size = getdirsize('D:/' + i)
        gbsize = '%.2f'%(size / 1024 / 1024 / 1024)
        list2.append(i)
        list2.append(float(gbsize))
        list1.append(list2)
    list1.sort(key=scondkey,reverse=True)
    print(list1)
