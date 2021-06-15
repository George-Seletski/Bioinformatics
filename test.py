from lxml import etree

coords = etree.parse("xml-test.xml").getroot()
coords_list = []

for coord in coords:
    this = {}
    for child in coord.getchildren():
        this[child.tag] = child.text
        coords_list.append(this)

for element in coords_list:
    print(element)
