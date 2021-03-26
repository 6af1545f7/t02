"""
This is an example of classes for a Person, with data, behaviour,
operator overloading and inheritance.
"""

__author__ = "6af1545f7"
__copyright__ = "6af1545f7"
__license__ = "mit"


class Person:
    """a general person
    """
    def __init__(self, name, age, pay=0, job=None):
        self.name = name
        self.age = age
        self.pay = pay
        self.job = job

    def lastName(self):
        return self.name.split()[-1]

    def giveRaise(self, percent):
        self.pay *= (1.0 + percent)

    def __str__(self):
        return '<%s => %s>' % (self.__class__.__name__, self.name)


class Manager(Person):
    """
    a person with custom raise inherits general lastname, str
    """
    def __init__(self, name, age, pay):
        Person.__init__(self, name, age, pay, 'manager')

    def giveRaise0(self, percent, bonus=0.1):
        self.pay *= (1.0 + percent + bonus)

    def giveRaise(self, percent, bonus=0.1):
        Person.giveRaise(self, percent + bonus)
        # example of calling 'class.method(instance, ...)'


def classTest() :
    bob = Person('Bob Smith', 42, 30000, 'software')
    sue = Person('Sue Jones', 45, 40000, 'hardware')
    sp0 = sue.pay
    sue.giveRaise(.10)
    sp1 = sue.pay
    tom = Manager(name='Tom Doe', age=50, pay=50000)
    tp0 = tom.pay
    tom.giveRaise(.20)
    tp1 = tom.pay
    r = {'name' : bob.name,
         'lastname' : sue.lastName(),
         'sue pay' : [sp0, sp1], 'tom pay' : [tp0, tp1]}
    return r


if __name__ == '__main__' :
    bob = Person('Bob Smith', 42, 30000, 'software')
    sue = Person('Sue Jones', 45, 40000, 'hardware')
    print(bob.name, sue.pay)
    print(bob.lastName())
    sue.giveRaise(.10)
    print(sue.pay)
    tom = Manager(name='Tom Doe', age=50, pay=50000)
    print(tom)
    tom.giveRaise(.20)
    print(tom.pay)

if __name__ == '__main__' :
    import shelve
    db = shelve.open('class-shelve')
    db['bob'] = bob
    db['sue'] = sue
    db['tom'] = tom
    db.close()

if __name__ == '__main__' :
    db = shelve.open('class-shelve')
    for key in db :
        print(key, '=>\n ', db[key].name, db[key].pay)
    bob = db['bob']
    print(bob.lastName())
    print(db['tom'].lastName())
