

# <7 ,3>  =>  3(2) 6(5) 2(1) 7(3) 5(2) 1(0) 4(0)
#    실질좌표   2    5     
#count로 숫자세서 알기 
# 리스트를 넘어갈떄 

"""
N , K = map(int, input().split())
ans=[] #정답출력 
data=[]
count = 0
for i in range(1,N+1):
    data.append(i)



while data:
    count = count + (K - 1) 
    if count >= len(data):
        count = count % len(data)

    ans.append(str(data.pop(count)))


    
print("<", ", ".join(ans),">", sep="") 

"""

from collections import deque

def josephus_problem(N, K):
    # 1부터 N까지 사람들 리스트
    people = deque(range(1, N+1))
    
    result = []
    
    while people:
        # K번째 사람을 제거해야 하므로, K-1번 만큼 큐에서 뒤로 이동
        people.rotate(-(K-1))
        # K번째 사람을 제거하고 결과에 추가
        result.append(people.popleft())
    
    return result

# 입력 받기
N, K = map(int, input().split())

# 요세푸스 순열 계산
result = josephus_problem(N, K)

# 출력 형식에 맞게 출력
print("<" + ", ".join(map(str, result)) + ">")



