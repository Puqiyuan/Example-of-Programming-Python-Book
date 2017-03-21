"""
test result:
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
from person import Person
from manager import Manager

bob = Person('Bob Smith', 42, 30000, 'software')
sue = Person('Sue Jones', 45, 40000, 'hardware')
tom = Manager('Tom Doe', 50, 50000)

db = shelve.open('class-shelve')
db['bob'] = bob
db['sue'] = sue
db['tom'] = tom
db.close()
