import sys
input() = sys.stdin.readline()
N = int(input())
lst=[]
for i in range(N):
    lst.append(input())

sorted_list = sorted(lst, key = lambda x : (len(x), x))

result = []
for i in sorted_list:
    if i not in result:
        result.append(i)
        print(i)
    else:
        continue