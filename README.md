# cveindex

A python tool to import data from various CVE lists to sqlite.

My first python project, potentially subject to breakage and inanity.


# Usage
`python3 ./main.py -s debian -s redhat -fi`

`-s` specifies the 'source' of the data, `-f` to fetch the data from its url,
`-i` to import to sqlite (`./cve.db`)

Currently provided data sources are:
- debian's [security-tracker][1] (`debian`)
- redhat's [Security Data API][2] (`redhat`) and [bugzilla][3]
(`redhat-bugzilla`)
- arch's [Vulnerable Issues][4] (`arch`)
- gentoo's [bugzilla][5] (`gentoo`)
- [Mitre][6] (`mitre`)

Some sources' public data may differ from what they actually have.

[1]: https://security-tracker.debian.org/tracker/
[2]: https://access.redhat.com/documentation/en/red-hat-security-data-api/version-0.1/red-hat-security-data-api/
[3]: https://salsa.debian.org/security-tracker-team/security-tracker/blob/master/data/CVE/list
[4]: https://security.archlinux.org/
[5]: https://bugs.gentoo.org/
[6]: https://cve.mitre.org/


# Adding sources
See `sources/skel/main.py` for an example template, and `sources/common.py`
for the Source class.
