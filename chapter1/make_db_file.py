"""
The test result:

pqy@sda1:~/.../chapter1$ ls
initdata.py  make_db_file.py  people-file  __pycache__/
pqy@sda1:~/.../chapter1$ python 
Python 3.5.2+ (default, Aug  5 2016, 08:07:14) 
[GCC 6.1.1 20160724] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> for line in open('people-file'):
...     print(line, end='')
... 
tom
job=>None
name=>'Tom'
age=>50
pay=>0
endrec.
sue
job=>'hdw'
name=>'Sue Jones'
age=>45
pay=>40000
endrec.
bob
job=>'dev'
name=>'Bob Smith'
age=>42
pay=>30000
endrec.
enddb.
>>> 
"""




dbfilename = 'people-file'
ENDDB = 'enddb.'
ENDREC = 'endrec.'
RECSEP = '=>'

def storeDbase(db, dbfilename=dbfilename):
    "formatted dump of database to flat file"
    dbfile = open(dbfilename, 'w')
    for key in db:
        print(key, file=dbfile)
        for (name, value) in db[key].items():
            print(name + RECSEP + repr(value), file=dbfile)
        print(ENDREC, file = dbfile)
    print(ENDDB, file = dbfile)
    dbfile.close()

def loadDbase(dbfilename = dbfilename):
    "parse data to reconstruct database"
    dbfile = open(dbfilename)
    import sys
    sys.stdin = dbfile
    db = {}
    key = input()
    while key != ENDDB:
        rec = {}
        field = input()
        while field != ENDREC:
            name, value = field.split(RECSEP)
            rec[name] = eval(value)
            field = input()
        db[key] = rec
        key = input()
    return db

if __name__ == '__main__':
    from initdata import db
    storeDbase(db)
