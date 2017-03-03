"""
The test result:
pqy@sda1:~/.../chapter1$ python3.5 make_db_shelve.py
pqy@sda1:~/.../chapter1$ python3.5 dump_db_shelve.py
bob =>
  {'name': 'Bob Smith', 'job': 'dev', 'pay': 30000, 'age': 42}
sue =>
  {'name': 'Sue Jones', 'job': 'hdw', 'pay': 40000, 'age': 45}
Sue Jones
"""

from initdata import bob, sue
import shelve
db = shelve.open('people-shelve')
db['bob'] = bob
db['sue'] = sue
db.close()
