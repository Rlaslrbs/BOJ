list = [0,0,0,0,0,0,0,0,0,0]

n = int(input())

for i in str(n):
    list[int(i)] += 1   


if (list[6] + list[9]) % 2 == 0: # 짝수 일 때
    list[6] = (list[6] + list[9]) // 2
    list[9] = list[6]
    if max(list) > list[6]:
        print(max(list))
    else:
        print(list[6])


else: # 홀수 일 때
    list[6] = (list[6] + list[9]) // 2 + 1
    list[9] = list[6]
    if max(list) > list[6]:
        print(max(list))
    else:
        print(list[6])




