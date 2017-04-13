"""
pqy@sda1:~/.../chapter1$ python make_db_classes.py 
pqy@sda1:~/.../chapter1$ python peopleinteract_query.py 
Key ? => name

No such key "name" !

Key ? => tom
name => Tom Doe
age  => 50
job  => None
pay  => 50000

Key ? => bob
name => Bob Smith
age  => 42
job  => software
pay  => 30000

Key ? =>
"""

import shelve

fieldnames = ('name', 'age', 'job', 'pay')
maxfield = max(len(f) for f in fieldnames)
db = shelve.open('class-shelve')

while True:
    key = input('\n Key ? => ')
    if not key: break
    try:
        record = db[key]
        
    except:
        print('No such key "%s" !' % key)

    else:
        for field in fieldnames:
            print(field.ljust(maxfield), '=>', getattr(record, field))
        
        
    
