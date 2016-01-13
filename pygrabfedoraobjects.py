__author__ = 'mbagget1'

import argparse
from lxml import etree


def createfile(filename):
    f = open(filename, 'w')
    results = etree.parse(fullSearchString).findall('//{http://www.fedora.info/definitions/1/0/types/}pid')
    for item in results:
        f.write(item.text)
    f.close()

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Use to specify a collection')
    parser.add_argument("-c", "--collection", dest="collection", help="namespace of collection", required=True)
    parser.add_argument("-l", "--link", dest="fedoraurl", help="url of fedora instance")
    parser.add_argument("-p", "--port", dest="portnumber", help="port number of fedora instance")
    parser.add_argument("-f", "--filename", dest="destfilename", help="name of file you want to save your set to")
    args = parser.parse_args()

    # Defaults
    fedoraurl = 'http://digital.lib.utk.edu'
    fedcollection = ''
    portnumber = ":8080"
    filename = "recordset.txt"

    if args.fedoraurl:
        fedoraurl = "http://{0}".format(args.fedoraurl)
    if args.collection:
        fedcollection = "{0}*".format(args.collection)
    if args.portnumber:
        portnumber = args.portnumber
    if args.destfilename:
        filenamedest = "{0}.txt".format(args.destfilename)

    fullSearchString = fedoraurl + ":8080/fedora/objects?query=pid%7E" + fedcollection + "&pid=true&resultFormat=xml"

    createfile(filename)