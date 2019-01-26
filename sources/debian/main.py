#!/bin/python3
import json
import re
from sources.common import *
from pprint import pprint

class Main(Source):
    def __init__(self, src="debian", url=None, path="data/debian", cves=None):
        super().__init__(src, url, path, cves)

    def Get(self):
        path    = self.path
        data    = json.load(open(path))
        cvelist = []

        for pkg, value in data.items():
            for cveid, svalue in value.items():
                    if cveid.startswith("CVE-"): #We don't really care about 'TEMP-'s
                        cvelist.append(CVE(str(cveid), 
                         str(pkg), str(svalue.get('description'))))

        import operator
        cvelist.sort(key=operator.attrgetter('id'))

        return cvelist

"""
def getcvelist():
    Source("debian", None, None, "debian/json")
    data = json.load(open('data/debian'))
    cvelist = []

    for pkg, value in data.items():
        for cveid, svalue in value.items():
                if cveid.startswith("CVE-"): #We don't really care about 'TEMP-'s
                    cvelist.append(CVE(str(cveid), str(pkg), str(svalue.get('description'))))

    import operator
    cvelist.sort(key=operator.attrgetter('id'))

    for value in cvelist:
        print("debian: %s: %s: %s" % (value.id, value.pkg, value.desc))

    return cvelist
"""
