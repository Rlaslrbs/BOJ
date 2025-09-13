import sys
import heapq
heap=[]
x = int(sys.stdin.readline())

for i in range(x):
    k = int(sys.stdin.readline())

    if k == 0 :
        if heap :
            print(heapq.heappop(heap))
        else:
            print('0')

    else:
        heapq.heappush(heap,k)