n = int(input())

data={}

lst=list(map(int,input().split()))

sorted_dict = sorted(list(set(lst)))
print(sorted_dict)

for i in range(len(sorted_dict)):
    data[sorted_dict[i]] = i

print(data)

for i in lst:
    print(data[i], end = ' ')
