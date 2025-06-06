#!/usr/bin/python3
"""serialization and deserialization
 using XML as an alternative format to JSON."""
import xml.etree.ElementTree as ET


def serialize_to_xml(dictionary: dict, filename: str):
    """serialize dictionary to xml"""
    root = ET.Element("data")
    for key in dictionary.keys():
        ET.SubElement(root, key).text = dictionary[key]
    tree = ET.ElementTree(root)
    tree.write(filename)


def deserialize_from_xml(filename):
    """deserialize xml to dictionary"""
    tree = ET.parse(filename)
    root = tree.getroot()

    data = {}
    for child in root:
        data[child.tag] = child.text
    return data
