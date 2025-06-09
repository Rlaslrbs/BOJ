import sys
input = sys.stdin.readline()

N = int(input())
cards = [*map(int,input().split())]
M = int(input())
targets =[*map(int,input().split())]


count = {}

for card in cards:
    if card in count:
        count[card] +=1
    else:
        count[card] = 1












lst=[]
for i in card:
    count = 0
    low = 0
    high = N - 1
    while low <= high:
        mid = (low + high // 2)
        if target[mid] < i:
            low = mid - 1
        elif target[mid] > i:
            high = mid + 1
        else:
            count +=1
            lst.append(count)

