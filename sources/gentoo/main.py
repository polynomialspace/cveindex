#!/bin/python3
import csv
from sources.common import *

# Dummy object to template from
class Main(Source):
    def __init__(self, src="gentoo", url=None, path=None, cves=None):
        super().__init__(src, url, path, cves)

    def Get(self):
        path    = self.path
        data    = csv.reader(open(path))
        cvelist = []

        for row in data:
            for cveid in row[1].split(','):
                cveid = cveid.strip()
                if cveid.__contains__("CVE"):
                    cvelist.append(CVE(cveid, "NULL", row[2]))
                #else:
                #    print("Invalid? '%s'"% (cveid))


        return cvelist
