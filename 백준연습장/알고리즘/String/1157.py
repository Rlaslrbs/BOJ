a =input()
k = list(a.upper())

count = {}

for char in k:
    if char in count:
        count[char] += 1
    else:
        count[char] = 1

m = 0
result =''
check = True
for char, count in count.items():
    if count > m:
        m = count
        result = char
        check = True
    elif count == m:
        result = '?'
        check = False

if check:
    print(result)
else:
    print(result)







"""
str=[]
count=[0] * len(k)

for i in range(0,len(k)):
    if k[i] not in str:
        str.append(k[i])
        count[i] += 1

    if k[i] in str:
        count[str.index(k[i])] +=1


m = max(count)

if count.count(m) >= 2:
    print('?')
else:
    print(str[count.index(m)])

"""