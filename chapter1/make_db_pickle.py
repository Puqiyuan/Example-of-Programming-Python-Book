"""
Test result:

pqy@sda1:~/.../chapter1$ python make_db_pickle.py 
pqy@sda1:~/.../chapter1$ python dump_db_pickle.py 
sue =>
  {'job': 'hdw', 'pay': 40000, 'age': 45, 'name': 'Sue Jones'}
bob =>
  {'job': 'dev', 'pay': 30000, 'age': 42, 'name': 'Bob Smith'}
tom =>
  {'job': None, 'pay': 0, 'age': 50, 'name': 'Tom'}
Sue Jones
"""



from initdata import db
import pickle
dbfile = open('people-pickle', 'wb')
pickle.dump(db, dbfile)
dbfile.close()
