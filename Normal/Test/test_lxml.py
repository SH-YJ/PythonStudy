from lxml import etree
import requests

if __name__ == '__main__':
    html = requests.get('https://2flj.xyz/')
    print(html)
    # xml = etree.parse('web5.xml',etree.XMLParser())
    # html1 = etree.HTML(html)
    # print(etree.tostring(html1, pretty_print=True).decode('utf-8'))
    # title = xml.xpath('//albumurl/text()')
    # print(title)
