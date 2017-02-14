"""
The result:

pqy@sda1:~/.../chapter1$ python update_db_pickle_recs.py 
pqy@sda1:~/.../chapter1$ python dump_db_pickle_recs.py 
tom.pkl =>
  {'name': 'Tom', 'age': 50, 'job': None, 'pay': 0}
bob.pkl =>
  {'name': 'Bob Smith', 'age': 42, 'job': 'dev', 'pay': 30000}
sue.pkl =>
  {'name': 'Sue Jones', 'age': 45, 'pay': 44000.0, 'job': 'hdw'}
Sue Jones
"""

import pickle
suefile = open('sue.pkl', 'rb')
sue = pickle.load(suefile)
suefile.close()

sue['pay'] *= 1.10
suefile = open('sue.pkl', 'wb')
pickle.dump(sue, suefile)
suefile.close
