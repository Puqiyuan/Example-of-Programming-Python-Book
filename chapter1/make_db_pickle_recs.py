"""
pqy@sda1:~/.../chapter1$ python make_db_pickle_recs.py 
pqy@sda1:~/.../chapter1$ python dump_db_pickle_recs.py 
tom.pkl =>
  {'name': 'Tom', 'job': None, 'age': 50, 'pay': 0}
bob.pkl =>
  {'name': 'Bob Smith', 'job': 'dev', 'age': 42, 'pay': 30000}
sue.pkl =>
  {'name': 'Sue Jones', 'job': 'hdw', 'age': 45, 'pay': 40000}
Sue Jones
"""

from initdata import bob, sue, tom
import pickle
for (key, record) in [('bob', bob), ('tom', tom), ('sue', sue)]:
    recfile = open(key + '.pkl', 'wb')
    pickle.dump(record, recfile)
    recfile.close()
