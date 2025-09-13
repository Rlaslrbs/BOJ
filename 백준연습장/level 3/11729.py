import heapq
import sys
n = int(input())

heap =[]
for i in range(n):
    k = int(sys.stdin.readline())

    if k:
        heapq.heappush(heap, (-k,k))
    else:
        if heap:
            print(heapq.heappop(heap)[1])
        else:
            print(0)