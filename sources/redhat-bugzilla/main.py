#!/bin/python3
import csv
from sources.common import *

class main(Source):
    def __init__(self, src="redhat-bugzilla", url=None, path=None, cves=None):
        super().__init__(src, url, path, cves)

    def Get(self):
        path    = self.path
        data    = csv.DictReader(open(path))
        cvelist = []

        for row in data:
                known  = row["Opened"]
                cveids = row["Alias"].split(',')
                pkg    = row["Component"] #Unreliable
                desc   = row["Summary"]

                for cveid in cveids:
                    cveid = cveid.strip()
                    if cveid.__contains__("CVE"):
                        cvelist.append(CVE(cveid, None, desc))
                    #else:
                    #    print("Invalid? '%s'"% (cveid))


        #for entry in cvelist:
        #    print("%s: %s: %s"% (entry.cveid, entry.pkg, entry.desc))
        return cvelist

    def Fetch(self, url=None, path=None):
        import requests

        if url == None:
            url = self.url
        if path == None:
            path = self.path

        urllist = url.split('\n')
        content = b""
        data = open(path, 'wb')
        for url in urllist:
            content += requests.get(url).content+b'\n'
        data.write(content)
        data.close()
