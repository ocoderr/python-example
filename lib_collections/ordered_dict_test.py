from collections import OrderedDict

user_dict =OrderedDict();
user_dict['a'] = 1
user_dict['b'] = 2
user_dict['c'] = 3

print(user_dict)

print(user_dict.popitem())  # 当成队列用
print(user_dict)

print(user_dict.move_to_end('a'))
print(user_dict)