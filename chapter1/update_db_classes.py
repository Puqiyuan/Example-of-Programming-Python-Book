"""
pqy@sda1:~/.../chapter1$ python make_db_classes.py                                                      
pqy@sda1:~/.../chapter1$ python update_db_classes.py                                                    
pqy@sda1:~/.../chapter1$ python dump_db_classes.py 
tom =>
  Tom Doe 65000.0
bob =>
  Bob Smith 30000
sue =>
  Sue Jones 50000.0
Smith
Doe
"""

import shelve
db = shelve.open('class-shelve')

sue = db['sue']
sue.giveRaise(.25)
db['sue'] = sue

tom = db['tom']
tom.giveRaise(.20)
db['tom'] = tom
db.close()
