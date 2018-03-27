from collections import defaultdict

users = ['name1', 'name2', 'name1', 'name3']
user_dict = defaultdict(int)  # 传递的是一个可调用的对象

for u in users:
    user_dict[u] += 1

print(user_dict)
