import argparse
from lxml import etree
import subprocess

parser = argparse.ArgumentParser(description='Use to specify a collection')
parser.add_argument("-p", "--parentnamespace", dest="parentnamespace", help="parent namespace of collection")
parser.add_argument("-l", "--link", dest="fedoraurl", help="url of fedora instance")
parser.add_argument("-f", "--filename", dest="destfilename", help="name of file you want to save your set to")
parser.add_argument("-dcr", "--dcrelation", dest="dcrelation", help="grab pids according to dc relation")
args = parser.parse_args()


def createfile(x):
    f = open(x, 'w')
    sessiontoken = ""
    recordcount = 0
    processresults(fullSearchString, f, sessiontoken, recordcount)


def processresults(url, f, sessiontoken, recordcount):
    document = etree.parse(url + sessiontoken)
    token = document.findall('//{http://www.fedora.info/definitions/1/0/types/}token')
    results = document.findall('//{http://www.fedora.info/definitions/1/0/types/}pid')
    recordcount += len(results)
    for item in results:
        f.write(item.text + "\n")
    if len(token) == 1:
        tokenval = document.findall('//{http://www.fedora.info/definitions/1/0/types/}token')[0].text
        sessiontoken = "&sessionToken=" + tokenval
        processresults(url, f, sessiontoken, recordcount)
    else:
        print("Done Processing. Wrote " + str(recordcount) + " records.")
        f.close()
        question = input("Update Solr from Results [y/N]")
        if question == "y":
            gsearchuser = input("Enter gsearch username:  ")
            gsearchpass = input("Enter gsearch password:  ")
            gsearchhost = input("Enter host name:  ")
            newsh = open("gsearchupdater.sh", 'w')
            newsh.write('FH=$FEDORA_HOME \nUSERNAME="' + gsearchuser + '"\nPASSWORD="' + gsearchpass + '"\nHOST="' + gsearchhost + '"\nPORT="8080"\nPROT="http"\nPIDS="gsearchupdater.sh"\n\n' + 'cat $PIDS | while read line; do\n   curl -XPOST -u"$USERNAME:$PASSWORD" "$PROT://$HOST:$PORT/fedoragsearch/rest?operation=updateIndex&action=fromPid&value=$line"\ndone')
            print('File was created.')
            newsh.close()
            subprocess.call('./gsearchupdater.sh', shell=True)
            print('\n\nProcess complete.')
        else:
            print("Exiting.")


if __name__ == "__main__":

    # Defaults
    fedoraurl = 'http://digital.lib.utk.edu'
    fedcollection = ''
    filename = "recordset.txt"
    dcrelation = ''

    if args.fedoraurl:
        fedoraurl = "http://{0}".format(args.fedoraurl)
    if args.parentnamespace:
        fedcollection = "pid%7E{0}*".format(args.parentnamespace)
    if args.destfilename:
        filenamedest = "{0}.txt".format(args.destfilename)
    if args.dcrelation:
        dcrelation = "relation%7E%27{0}%27".format(args.dcrelation).replace(" ", "%20")

    fullSearchString = fedoraurl + ":8080/fedora/objects?query=" + fedcollection + dcrelation + "&pid=true&resultFormat=xml"

    createfile(filename)

