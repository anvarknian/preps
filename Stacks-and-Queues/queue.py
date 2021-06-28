### With import
from collections import deque
queue1 = deque()
queue1.append(1)
queue1.append(2)
queue1.append(3)
queue1.append(4)
queue1.append(5)

print(queue1.popleft())
print(queue1.popleft())
print(queue1.popleft())
print(queue1.popleft())
print(queue1.popleft())

print("###############")

### With no import
queue2 = []
queue2.append(1)
queue2.append(2)
queue2.append(3)
queue2.append(4)
queue2.append(5)
queue2.reverse()

print(queue2.pop())
print(queue2.pop())
print(queue2.pop())
print(queue2.pop())
print(queue2.pop())