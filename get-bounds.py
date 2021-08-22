import re 
from sys import argv
from xml.etree import ElementTree as ET 

# args:
#1: xml file name
#2*i: attr string 
#2*i+1: attr value string
tree = ET.parse(argv[1])
root = tree.getroot() 


for p in root.findall('.//node'):
    # find bounds for matched associated attr string and attr value
    match = all([argv[i] in p.attrib and p.attrib[argv[i]]==argv[i+1] for i in range(2,len(argv),2)])
    if match:
        result = p.attrib["bounds"]



m = re.match(r"\[(\d+),(\d+)\]\[(\d+),(\d+)\]", result)
if m:
    x1 = int(m.group(1))
    y1 = int(m.group(2))
    x2 = int(m.group(3))
    y2 = int(m.group(4))
    print((x1+x2)/2, (y1+y2)/2)