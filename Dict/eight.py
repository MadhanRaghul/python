#deleting using del method and popitem()

emps={'name':'Ezio',
      'loc':'Italy',
      'role':'Master Assassin',
      'email':'ezio@gmail.com'}

del emps['name']
print(emps)

emps.popitem()      #pop will remove a random keys in the dict
print(emps)