__author__ = 'mbagget1'

import argparse
from lxml import etree

parser = argparse.ArgumentParser(description='Use to specify a collection')
parser.add_argument("-c", "--collection", dest="collection", help="namespace of collection", required=True)
parser.add_argument("-l", "--link", dest="fedoraurl", help="url of fedora instance")
parser.add_argument("-p", "--port", dest="portnumber", help="port number of fedora instance")
parser.add_argument("-f", "--filename", dest="destfilename", help="name of file you want to save your set to")
parser.add_argument("-a", "--appendtoexistingfile", dest="appendtofile", help="use this option if you are appending to an existing file")
args = parser.parse_args()

def createfile(filename):
    f = open(filename, 'w')
    document = etree.parse(fullSearchString)
    #root = document.getroot()
    #print(document.('//{http://www.fedora.info/definitions/1/0/types/}token')[0].text)
    token = document.findall('//{http://www.fedora.info/definitions/1/0/types/}token')
    #print(token[0].text)
    processresults(document, fullSearchString, f, token)

def processresults(document, fullSearchString, f, token):
    token = document.findall('//{http://www.fedora.info/definitions/1/0/types/}token')
    #print(len(token))
    results = document.findall('//{http://www.fedora.info/definitions/1/0/types/}pid')
    for item in results:
        f.write(item.text)
    f.close()
    if len(token) == 1:
        tokenval = document.findall('//{http://www.fedora.info/definitions/1/0/types/}token')[0].text
        sessiontoken = "&sessionToken=" + tokenval
        newsessiontoken = open('sessiontoken.txt', 'w')
        newsessiontoken.write(sessiontoken)
        newsessiontoken.close()
        print("Still Processing!!!")
    else:
        print("Done Processing")

def appendfile(filename, fullSearchString):
    appendfile = open(filename, 'a')
    sessiontoken = open('sessiontoken.txt', 'r').read()
    fullSearchString = fullSearchString + sessiontoken
    #print(fullSearchString)
    document = etree.parse(fullSearchString)
    token = document.findall('//{http://www.fedora.info/definitions/1/0/types/}token')
    results = document.findall('//{http://www.fedora.info/definitions/1/0/types/}pid')
    for item in results:
        appendfile.write(item.text)
    appendfile.close()
    if len(token) == 1:
        tokenval = document.findall('//{http://www.fedora.info/definitions/1/0/types/}token')[0].text
        sessiontoken = "&sessionToken=" + tokenval
        newsessiontoken = open('sessiontoken.txt', 'w')
        newsessiontoken.write(sessiontoken)
        newsessiontoken.close()
        print("Still Processing!!!")
    else:
        print("Done Processing!!!")


if __name__ == "__main__":

    # Defaults
    fedoraurl = 'http://digital.lib.utk.edu'
    fedcollection = ''
    portnumber = ":8080"
    filename = "recordset.txt"
    process = 0

    if args.fedoraurl:
        fedoraurl = "http://{0}".format(args.fedoraurl)
    if args.collection:
        fedcollection = "{0}*".format(args.collection)
    if args.portnumber:
        portnumber = args.portnumber
    if args.destfilename:
        filenamedest = "{0}.txt".format(args.destfilename)
    if args.appendtofile:
        process = 1

    fullSearchString = fedoraurl + ":8080/fedora/objects?query=pid%7E" + fedcollection + "&pid=true&resultFormat=xml"

    if process == 0:
        createfile(filename)
    if process == 1:
        appendfile(filename, fullSearchString)
