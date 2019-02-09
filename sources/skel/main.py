#!/bin/python3
from sources.common import *

# Dummy object to template from
class main(Source):
    def __init__(self, src="skel", url=None, path=None, cves=None):
        super().__init__(src, url, path, cves)

    def Get(self):
        path    = self.path
        data    = open(path).read()
        cvelist = []

        d1, d2, d3 = data.split()
        cvelist.append(CVE(d1, d2, d3))

        return cvelist

    # Write dummy data since we have no real data to fetch
    # You probably don't need to redefine this in an actual module
    def Fetch(self, url=None, path=None):
        path = self.path

        data = open(path, 'wb')
        data.write(b"CVE-0001-9999 SOME-PACKAGE SOME-CVE-DESCRIPTION\n")
        data.close()
