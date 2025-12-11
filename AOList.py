import requests
import xml.etree.ElementTree as ET
from urllib import parse

def listFileUrls(url):
  p = parse.urlparse(url)
  path = p.path.split("/")
  if path[1] == "details" or path[1] == "download":
    rootpath = p.scheme+"://"+p.netloc+"/download/"+path[2]+"/"
    xml = requests.get(rootpath+path[2]+"_files.xml").text
    root = ET.fromstring(xml)
    path = []
    for child in root:
      path.append(rootpath+parse.quote(child.attrib['name']).replace(" ", "%20"))

    return path
  else:
    raise("Path Invalid")


def listFileTypeUrls(url, filetype="iso"):
  urls = listFileUrls(url)
  list = []
  for url in urls:
    if url.split(".").pop() == filetype:
      list.append(url)
  return list
