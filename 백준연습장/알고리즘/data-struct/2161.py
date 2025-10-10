
from collections import deque   

n = int(input())
dq = deque(range(1, n+1))

result = []
while dq:
    result.append(dq.popleft())
    if dq:
        dq.append(dq.popleft()) 

print(*result) 