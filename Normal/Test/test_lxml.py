from lxml import etree
import requests

if __name__ == '__main__':
    xml = etree.parse('web5.xml',etree.XMLParser())
    html1 = etree.HTML(xml)
    print(etree.tostring(html1, pretty_print=True).decode('utf-8'))
    title = xml.xpath('//albumurl/text()')
    print(title)
