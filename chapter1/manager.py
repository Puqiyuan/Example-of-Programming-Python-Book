"""
This program test for inheritance in Python. The Manager class re-implement give Raise method
of Person class.

Test result:
pqy@sda1:~/.../chapter1$ python3.5 manager.py
Doe
65000.0
"""

from person import Person

class Manager(Person):
    def giveRaise(self, percent, bonus = 0.1):
        self.pay *= (1.0 + percent + bonus)

if __name__ == '__main__':
    tom = Manager(name = 'Tom Doe', age = 50, pay = 50000)
    print(tom.lastName())
    tom.giveRaise(.20)
    print(tom.pay)
    
            
