from xml.dom import minidom


def beautifyXMLString(xmlString):
    print(minidom.parseString(xmlString).toprettyxml())
    return minidom.parseString(xmlString).toprettyxml()[23:]


xml = '<x><a>bbb</a><c>ddd</c></x>'
print(beautifyXMLString(xml))
