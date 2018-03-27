from collections import namedtuple

User = namedtuple("User", ["name", 'age'])
user = User("name", 13)
print(user.name, user.age)
