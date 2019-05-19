#!/bin/python3
import json
from sources.common import *

class Main(Source):
    def __init__(self, src="arch", url=None, path=None, cves=None):
        super().__init__(src, url, path, cves)

    def get(self):
        path    = self.path
        data    = json.load(open(path))
        cvelist = []

        for entry in data:
            for cveid in entry.get('issues'):
                pkg = str(entry.get('packages')[0])
                desc = pkg + "-" + str(entry.get('affected')) + ": " + str(entry.get('type'))

                cvelist.append(CVE(cveid, pkg, desc))

        return cvelist
