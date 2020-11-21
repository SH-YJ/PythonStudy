from lxml import etree

if __name__ == '__main__':
    xml = etree.parse('web5.xml',etree.XMLParser())
    print(etree.tostring(xml, pretty_print=True).decode('utf-8'))
    title = xml.xpath('//albumurl/text()')
    print(title)
