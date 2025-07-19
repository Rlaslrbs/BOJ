t = int(input())

for _ in range(t):
    closet={}
    c = int(input())
    for _ in range(c):
        wear = list(input().split())
        if wear[1] in closet:
            closet[wear[1]].append(wear[0])
        else:
            closet[wear[1]] = [wear[0]]
    count = 1
    for k in closet:
        count = count*(len(closet[k])+1)
    print(count-1)


        
