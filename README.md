# cveindex

A python tool to import data from various CVE lists to sqlite.

My first python project, so probably very messy.


# Usage
`./python3 main.py -s debian -s redhat -fi`

-s specifies the 'source' of the data, -f to fetch the data from its url,
-i to import to sql

Currently there are only 2 sources provided, from debian's
[security-tracker][1] and redhat's [Securty Data API][2].

Both tend to be outdated from what Debian and Redhat *actually* have.
I plan to write additial modules to fetch from debian's [source data][3]
and Redhat's bugzilla. MITRE and others are on the TODO list as well.

[1]: https://security-tracker.debian.org/tracker/
[2]: https://access.redhat.com/documentation/en/red-hat-security-data-api/version-0.1/red-hat-security-data-api/
[3]: https://salsa.debian.org/security-tracker-team/security-tracker/blob/master/data/CVE/list


# Adding sources
If you wish to add additional data sources, it should be as easy as using 
the following template, and dropping it in `sources/somename/main.py`:

```
class Main(Source):
        def __init__(self, src="somename", url=None, path="data/somename", cves=None):
                super().__init__(src, url, path, cves)
        def Get(self):
                # Whatever code to parse the data
```
See `sources/common.py` for the Source class. 


This, again, being my first project in python, may be subject to breakage whenever
I figure out how I actually want everything to work
