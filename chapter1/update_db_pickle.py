"""
The result:
pqy@sda1:~/.../chapter1$ python update_db_pickle.py 
pqy@sda1:~/.../chapter1$ python dump_db_pickle.py 
sue =>
  {'age': 45, 'job': 'hdw', 'pay': 44000.0, 'name': 'Sue Jones'}
tom =>
  {'age': 50, 'job': None, 'pay': 0, 'name': 'Tom Tom'}
bob =>
  {'age': 42, 'job': 'dev', 'pay': 30000, 'name': 'Bob Smith'}
Sue Jones

"""

import pickle
dbfile = open('people-pickle', 'rb')
db = pickle.load(dbfile)
dbfile.close()

db['sue']['pay'] *= 1.10
db['tom']['name'] = 'Tom Tom'

dbfile = open('people-pickle', 'wb')
pickle.dump(db, dbfile)
dbfile.close()
