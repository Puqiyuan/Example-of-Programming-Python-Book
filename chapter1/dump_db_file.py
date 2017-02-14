"""
The test result:

pqy@sda1:~/.../chapter1$ python dump_db_file.py 
sue =>
  {'pay': 40000, 'job': 'hdw', 'age': 45, 'name': 'Sue Jones'}
tom =>
  {'pay': 0, 'job': None, 'age': 50, 'name': 'Tom'}
bob =>
  {'pay': 30000, 'job': 'dev', 'age': 42, 'name': 'Bob Smith'}
Sue Jones
"""


from make_db_file import loadDbase
db = loadDbase()
for key in db:
    print(key, '=>\n ', db[key])
print(db['sue']['name'])
