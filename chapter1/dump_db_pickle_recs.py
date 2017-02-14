"""
Test result:

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


import pickle, glob
for filename in glob.glob('*.pkl'):
    recfile = open(filename, 'rb')
    record = pickle.load(recfile)
    print(filename, '=>\n ', record)

suefile = open('sue.pkl', 'rb')
print(pickle.load(suefile)['name'])
