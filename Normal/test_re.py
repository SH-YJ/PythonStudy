import re

text = "我是你**??<>:asdas！\"！"


def Judge(t):
    pattern = ("[^a-zA-Z0-9_\u4e00-\u9fa5]+")
    a = re.search(pattern, t)
    if a is not None:
        return True


# < > / \ | : " * ?
if Judge(text) is True:
    t1 = text
    li = ['<', '>', '/', '\\', ':', '?', '*','"']
    for i in li:
        t1 = t1.replace(i, '')
    print(t1)
