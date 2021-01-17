#Generator for UniProt entries
from lmxl import etree

def get_entries(f):
    entry = ''
    for line in f:
        line = line.decode()
        if line.startswith("<entry"):
            entry = ''
        entry += line
        if line.startswith("</entry>"):
            yield entry
            entry = ''


def parse_xml_entry(xml):
    root = etree.fromstring(xml)
    accession = root.find("accession", root.nsmap).text
    annotations = []
    for dbReference in root.findall("dbReference", root.nsmap):
        if dbReference.get("type") == "GO":
            annotations.append(dbReference.get("id"))
    return accession, annotations