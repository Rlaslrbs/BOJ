import sys
from collections import deque
input = sys.stdin.readlines

n = int(input())
p = round(n*(3/20))
data=[]

for i in range(n):
    data.append(int(input()))

data.sort()
dq = deque(data)

for _ in range(p):
    dq.popleft()
    dq.pop()
avg = (sum(dq) / len(dq))

if avg - int(avg) < 0.4:
    print(int(avg))
else:
    print(int(avg)+1)

