isbn = input() #텍스트 

m = int(isbn[-1]) #7

f = 0 
count = 1
unknown_weight = 0
for i in isbn[:-1]:
    if i == '*':
        if count % 2 == 0: #짝수
            unknown_weight = 3
            count+=1
        else:
            unknown_weight = 1
            count+=1
    else:
        if count % 2 == 0: #짝수
            f+= int(i) * 3
            count+=1
        else:
            f+=int(i) 
            count+=1


for i in range(10):
    result = (f + (unknown_weight * i) + m ) % 10

    if result == 0:
        print(i)
        break


            

















