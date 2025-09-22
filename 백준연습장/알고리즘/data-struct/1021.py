from collections import deque
import sys

input = sys.stdin.readline

n , m = map(int,input().split())
position = list(map(int,input().split()))

dq = deque([i for i in range(1,n+1)])
count = 0
for i in position:
    while True:
        if dq[0] == i:
            dq.popleft()
            break
        else:
            if dq.index(i) < len(dq)/2: # 왼쪽에 있을때
                while dq[0] != i:
                    dq.append(dq.popleft())
                    count+=1
            else: #오른쪽에 있을떄 
                while dq[0] != i:
                    dq.appendleft(dq.pop())
                    count+=1


print(count)

