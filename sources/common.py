class CVE(object):
    def __init__(self, cveid=None, pkg=None, desc=None):
        self.pkg = pkg
        self.desc = desc
        self.cveid = cveid

class Source(object):
    def __init__(self, src=None, url=None, path=None, cves=None):
        self.src = src

        if url is None:
            url = open("sources/%s/url"%(src)).read().strip('\n')
        self.url = url

        if path is None:
            path = "data/%s"%(src)
        self.path = path

        self.cves = CVE(cves)

    def fetch(self, url=None, path=None):
        import requests

        if url is None:
            url = self.url
        if path is None:
            path = self.path

        data = open(path, 'wb')
        content = requests.get(url).content
        data.write(content)
        data.close()

    def get(self):
        _ = self
