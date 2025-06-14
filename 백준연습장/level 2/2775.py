T = int(input())

for i in range(T):
    k = int(input())
    n = int(input())

# 0층
    people=[]
    sum_people = 0
    for i in range(1,n+1):
        people.append(i)

#1층 이상  
    for i in range(k):
        for i in range(1, n):
            people[i] = people[i] + people[i-1]


        


    print(people[(n-1)])

#1
#    1 2 3
#0층 1 2 3
#1층 1 3 6
#2층 1 4 10
#3층 1 5 15 
#4층 1 6 21
