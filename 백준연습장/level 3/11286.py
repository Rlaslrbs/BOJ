import sys
import heapq
heap=[]
n = int(sys.stdin.readline())

for i in range(n):
    k = int(sys.stdin.readline())

    if k:
        heapq.heappush(heap, (abs(k),k))
    else: #k가 0일때
        if heap:
            print(heapq.heappop(heap)[1])
        else:
            print(0)

