from collections import deque

user_deque = deque([1,2,3,4])
user_deque.appendleft(0)
print(user_deque)

v = user_deque.popleft()
print(v,user_deque)