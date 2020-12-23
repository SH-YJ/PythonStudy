import re

text = "我是你**??<>:asdas！\"！"


def Judge(t):
    pattern = ("[^a-zA-Z0-9_\u4e00-\u9fa5]+")
    a = re.search(pattern, t)
    if a is not None:
        return True


# < > / \ | : " * ?
# t1 = text
# li = ['<', '>', '/', '\\', ':', '?', '*', '"']
# if Judge(text) is True:
#     for i in li:
#         t1 = t1.replace(i, '')
# print(t1)

if __name__ == '__main__':
    list1 = ['第三百七十一章 得意', '第三百七十一章  得意','第三百七十一章   得意','第三百七十一章    得意']
    list2 = []
    for i in list1:
        list2.append(i.replace(' ','#'))
    print(list2)