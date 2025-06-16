"""
n = int(input())
card=[]
for i in range(1,n+1):
    card.append(i)

while len(card) > 1:
    card.pop(0)
    card.append(card.pop(0))

print(card[0])
"""    

from collections import deque

n = int(input())
dq = deque()

for i in range(1,n+1):
    dq.append(i)

while len(dq) > 1:
    dq.popleft()
    dq.append(dq.popleft())

print(dq[0])

