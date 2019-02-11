#!/bin/python3
import sys

def fetchdata(sources):
    for source in sources:
        print("%s: fetching from '%s' to '%s'." % (source.src, source.url, source.path))
        source.fetch()


def importdata(sources, dbname):
    import sqlite3
    conn = sqlite3.connect(dbname)
    cur = conn.cursor()

#    conn.set_trace_callback(print)

    for source in sources:
        print("%s: Importing data from '%s' to '%s'."% (source.src, source.path, dbname))
        cur.execute(
            """
            DROP TABLE IF EXISTS "%s";
            """%
            (source.src)
        )

        cur.execute(
            """
            CREATE TABLE IF NOT EXISTS "%s" (
            id      INTEGER  PRIMARY KEY  AUTOINCREMENT,
            cveid   VARCHAR  NOT NULL,
            package VARCHAR,
            desc    VARCHAR
            );
            """%
            (source.src)
        )

        for cve in source.get():
            #print("ID:%s\nPKG:%s\nDSC:%s\n" % (cve.id, cve.pkg, cve.desc))
            cur.execute(
                """
                INSERT INTO "%s" VALUES(NULL, ?, ?, ?)
                """%
                (source.src),
                (cve.cveid, cve.pkg, cve.desc)
            )
        cur.execute("commit")
    conn.close()

#def CompareData(cmp1, cmp2):
#    conn = sqlite3.connect('cve.db')
#    cur  = conn.cursor()
#
#    cur.execute(
#    """
#    SELECT DISTINCT cveid,desc FROM %s WHERE cveid NOT IN
#    (SELECT DISTINCT cveid FROM %s)
#    """%
#    (cmp1, cmp2)
#    )
#
#    for row in cur.fetchall():
#        for val in row:
#            print("IN %s NOT %s: %s"% (cmp1, cmp2, str(val)))
#

def main(argv):
    import getopt
    import importlib

    sources = []
    dbname = "cve.db"
    fetch = False
    imprt = False # 😶

    try:
        opts, arg = getopt.getopt(argv, "fis:")
    except getopt.getoptError:
        print("")
        sys.exit(2)

    for opt, arg in opts:
        if   opt == '-f':
            fetch = True
        elif opt == '-i':
            imprt = True
        elif opt == '-s':
            sources.append(importlib.import_module("sources.%s.main"%arg).Main())

    if fetch:
        fetchdata(sources)
    if imprt:
        importdata(sources, dbname)


if __name__ == "__main__":
    main(sys.argv[1:])
