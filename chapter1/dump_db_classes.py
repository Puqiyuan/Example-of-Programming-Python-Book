"""
pqy@sda1:~/.../chapter1$ python make_db_classes.py 
pqy@sda1:~/.../chapter1$ python dump_db_classes.py 
tom =>
  Tom Doe 50000
bob =>
  Bob Smith 30000
sue =>
  Sue Jones 40000
Smith
Doe
"""

import shelve
db = shelve.open('class-shelve')
for key in db:
    print(key, '=>\n ', db[key].name, db[key].pay)

bob = db['bob']
print(bob.lastName())
print(db['tom'].lastName())
    
