import sys

n = int(sys.stdin.readline())

lst = list(map(int,sys.stdin.readline().split()))

sum = 0

for i in range(len(lst)):
    temp = 0
    for j in range(i,len(lst)):
        temp += abs(lst[i]-lst[j])
    sum+=temp*2
print(sum)














'''
1 5 = 4
1 3 = 2
1 2 = 1
1 4 = 3

5 1 = 4
5 3 = 2
5 2 = 3 
5 4 = 1

3 1 = 2
3 5 = 2
3 2 = 1
3 4 = 1

2 1
2 5
2 3
2 4

4 1
4 5
4 3
4 2


'''