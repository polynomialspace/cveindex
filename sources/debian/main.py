#!/bin/python3
import json
from sources.common import *

class Main(Source):
    def __init__(self, src="debian", url=None, path="data/debian", cves=None):
        super().__init__(src, url, path, cves)

    def get(self):
        path = self.path
        data = json.load(open(path, encoding='utf-8'))
        cvelist = []

        for pkg, value in data.items():
            for cveid, svalue in value.items():
                if cveid.startswith("CVE-"): #We don't really care about 'TEMP-'s
                    cvelist.append(CVE(str(cveid),
                                       str(pkg), str(svalue.get('description'))))

        import operator
        cvelist.sort(key=operator.attrgetter('cveid'))

        return cvelist
