#!/usr/bin/env python3
import xml.etree.ElementTree as ET

def serialize_to_xml(dictionary, filename):
    root = ET.Element("dict_data")
    for key, value in dictionary.items():
        child = ET.SubElement(root, key)
        child.text = str(value)
    tree = ET.ElementTree(root)
    tree.write(filename, encoding="utf-8", xml_declaration=True)

def deserialize_from_xml(filename):
    tree = ET.parse(filename)
    root = tree.getroot()
    py_dict = {child.tag: child.text for child in root}

    return py_dict