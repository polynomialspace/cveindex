#!/bin/python3
import json
import re
from sources.common import *
from pprint import pprint

class main(Source):
    def __init__(self, src="redhat", url=None, path="data/redhat", cves=None):
        super().__init__(src, url, path, cves)


    def Get(self):
        path = self.path
        data = json.load(open(path))
        cvelist = []

        for entry in data:
            cvelist.append(CVE(str(entry.get('CVE')), str(entry.get('affected_packages')),
            str(entry.get('bugzilla_description').strip())))
            #cvelist.append(CVE(key.get, pkg, svalue.get('description')))

        import operator
        cvelist.sort(key=operator.attrgetter('cveid'))

        return cvelist
