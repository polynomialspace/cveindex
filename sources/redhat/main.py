#!/bin/python3
import json
from sources.common import *

class Main(Source):
    def __init__(self, src="redhat", url=None, path="data/redhat", cves=None):
        super().__init__(src, url, path, cves)


    def get(self):
        path = self.path
        data = json.load(open(path, encoding='utf-8'))
        cvelist = []

        for entry in data:
            cvelist.append(CVE(str(entry.get('CVE')), str(entry.get('affected_packages')),
                               str(entry.get('bugzilla_description').strip())))
            #cvelist.append(CVE(key.get, pkg, svalue.get('description')))

        import operator
        cvelist.sort(key=operator.attrgetter('cveid'))

        return cvelist
