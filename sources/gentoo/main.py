#!/bin/python3
import csv
from sources.common import *

class main(Source):
    def __init__(self, src="gentoo", url=None, path=None, cves=None):
        super().__init__(src, url, path, cves)

    def Get(self):
        path    = self.path
        data    = csv.DictReader(open(path))
        cvelist = []

        for row in data:
                known  = row["Opened"]
                cveids = row["Alias"].split(',')
                pkg    = row["Package list"] #Unreliable
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
