"""
The test result:
pqy@sda1:~/.../chapter1$ python update_db_file.py 
pqy@sda1:~/.../chapter1$ python dump_db_file.py 
tom =>
  {'job': None, 'name': 'Tom Tom', 'pay': 0, 'age': 50}
sue =>
  {'job': 'hdw', 'name': 'Sue Jones', 'pay': 44000.0, 'age': 45}
bob =>
  {'job': 'dev', 'name': 'Bob Smith', 'pay': 30000, 'age': 42}
Sue Jones
"""


from make_db_file import loadDbase, storeDbase
db = loadDbase()
db['sue']['pay'] *= 1.10
db['tom']['name'] = 'Tom Tom'
storeDbase(db)
