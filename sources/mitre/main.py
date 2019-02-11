#!/bin/python3
import csv
from sources.common import *

class Main(Source):
    def __init__(self, src="mitre", url=None, path=None, cves=None):
        super().__init__(src, url, path, cves)

    def get(self):
        path = self.path
        # This should maybe be converted to DictReader?
        data = csv.reader(open(path, encoding="ISO-8859-1")) # 😶 😶 😶
        cvelist = []

        for row in data:
            if row[0].startswith("CVE"):
                if not row[2].startswith("** RESERVED **"):
                    # mitre doesn't provide source/package info as it doesnt
                    # apply a lot of the time, and descriptions are too
                    # varadic to sanely parse it.
                    cvelist.append(CVE(row[0], "NULL", row[2]))

        return cvelist
