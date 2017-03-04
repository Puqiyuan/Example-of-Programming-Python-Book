"""
pqy@sda1:~/.../chapter1$ python3.5 dump_db_shelve.py 
bob =>
  {'pay': 30000, 'age': 42, 'name': 'Bob Smith', 'job': 'dev'}
sue =>
  {'pay': 40000, 'age': 45, 'name': 'Sue Jones', 'job': 'hdw'}
Sue Jones
pqy@sda1:~/.../chapter1$ python3.5 update_db_shelve.py
pqy@sda1:~/.../chapter1$ python3.5 dump_db_shelve.py 
tom =>
  {'job': None, 'age': 50, 'pay': 0, 'name': 'Tom'}
bob =>
  {'job': 'dev', 'age': 42, 'pay': 30000, 'name': 'Bob Smith'}
sue =>
  {'job': 'hdw', 'age': 45, 'pay': 60000.0, 'name': 'Sue Jones'}
Sue Jones
pqy@sda1:~/.../chapter1$ 
"""


from initdata import tom
import shelve
db = shelve.open('people-shelve')
sue = db['sue']
sue['pay'] *= 1.50
db['sue'] = sue
db['tom'] = tom
db.close()
