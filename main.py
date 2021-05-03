import xml.etree.ElementTree as Et

tree = Et.parse("xml-test.xml")
root = tree.getroot()

for child in root:
	print(child.tag, child.attrib)
