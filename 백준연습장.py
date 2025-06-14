# -*- coding: utf-8 -*-
"""백준연습장.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1vmXTTMacoBMURZeP91D_GKVdaC6zqejF

# **2025-05-07**
"""

a,b = map(int, intput().split())
print(a/b)

a,b = map(int, input().split())
print(a/b)

a,b = map(int, input().split())
print(a+b)
print(a-b)
print(a*b)
print(int(a/b))
print(a%b)

x=input()
print(x+'??!')

y = int(input(""))
x = y - (2541 - 1998)
print(x)

A,B,C= map(int,input().split())
print((A+B)%C)
print(((A%C) + (B%C))%C)
print((A*B)%C)
print(((A%C)*(B%C))%C)

a,b,c=map(int,input())
x,y,z=map(int,input())

print((100*a+10*b+c)*z)
print((100*a+10*b+c)*y)
print((100*a+10*b+c)*x)
print((100*a+10*b+c)*(100*x+10*y+z))

a,b,c=map(int,input().split())
print(a+b+c)

X = int(input(""))
N = int(input(""))
sum = 0
for i in range(N):
  price, num = map(int, input().split())
  sum += (price*num)

if sum == X:
  print("Yes")

else:
  print("No")

"""# **2025-05-09**"""

N = int(input(""))

for i in range(N//4):
  print("long", end=' ')

print("int")

import sys  # sys모듈 읽어들이기

t = int(sys.stdin.readline())

for _ in range(t):
    a,b = map(int, sys.stdin.readline().split())
    print(a+b)

"""한 두줄 입력받는 문제들과 다르게, 반복문으로 여러줄을 입력 받아야 할 때는 input()으로 입력 받는다면 시간초과가 발생할 수 있습니다. 대표적인 예시가 백준 BOJ 15552번 문제입니다.

📌정해진 개수의 정수를 한줄에 입력받을 때
import sys
a,b,c = map(int,sys.stdin.readline().split())
map()은 반복 가능한 객체(리스트 등)에 대해 각각의 요소들을 지정된 함수로 처리해주는 함수입니다.
위와 같이 사용한다면 a,b,c에 대해 각각 int형으로 형변환을 할 수 있습니다.

📌 임의의 개수의 정수를 한줄에 입력받아 리스트에 저장할 때
import sys
data = list(map(int,sys.stdin.readline().split()))
split()은 문자열을 나눠주는 함수입니다.
괄호 안에 특정 값을 넣어주면 그 값을 기준으로 문자열을 나누고, 아무 값도 넣어주지 않으면 공백(스페이스, 탭, 엔터 등)을 기준으로 나눕니다.

list()는 자료형을 리스트형으로 변환해주는 함수입니다.
map()은 맵 객체를 만들기 때문에, 리스트형으로 바꿔주기 위해서 list()로 감싸주었습니다.

📌 임의의 개수의 정수를 n줄 입력받아 2차원 리스트에 저장할 때
import sys
data = []
n = int(sys.stdin.readline())
for i in range(n):
    data.append(list(map(int,sys.stdin.readline().split())))
이렇게 한다면 각 요소의 길이가 동일한 2차원 리스트도 만들 수 있고,
각각 길이가 다른 2차원 리스트도 입력 받을 수 있습니다.
"""

T = int(input())
k=0
for i in range(T):
  a,b = map(int, input().split())
  k+=1
  print("Case #" + str(k) + ":" , a+b)

T = int(input())
k=0
for i in range(T):
  a,b = map(int, input().split())
  k+=1
  print("Case #" + str(k) + ":",a,"+",b,"=",a+b)

n = int(input())

for i in range(1,n+1):
  print('1' * (n-i) + '*' * i)

sum=1
while sum > 0:
  a,b = map(int,input().split())
  sum=a+b
  if sum > 0 :
    print(sum)

while True:
  try:
    a,b = map(int,input().split())
    print(a+b)
  except:
    break

N = int(input())
n_list = list(map(int, input().split()))
v = int(input())

print(n_list.count(v))

"""# **2025-05-10**"""

n, x =map(int, input().split())
n_list = list(map(int, input().split()))
for i in range(n):
  if n_list[i] < x:
    print(n_list[i], end=" ")

N = int(input())
n_list=list(map(int,input().split()))
max=0
min=0
for i in range(n_list):
  if i > max:
    max = i

for i in range(n_list):
  if i < min:
    min = i

print(min, max)

"""min(lst), max(lst) 최대 최소 출력

"""

2342

N, M  = map(int, input().split())

bucket = [0]*(N+1)

for a in range(M):
  i,j,k = map(int, input().split())
  for b in range(i-1,j):
    bucket[b] = k

for c in range(N):
  print(bucket[c], end=" ")

"""# **2025-05-12**"""



N, M = map(int, input().split())

k = 0
bucket = []
for a in range(1,N+1):
  bucket.append(a)

temp = 0

for b in range(M):
  i,j = map(int, input().split())
  temp = bucket[i-1]
  bucket[i-1] = bucket[j-1]
  bucket[j-1] = temp

for c in range(N):
  print(bucket[c], end=" ")

lst1=[]
lst2=[]

for i in range(1,31):
  lst1.append(i)


for i in range(28):
  a=int(input())
  lst2.append(a)

s1 = set(lst1)
s2 = set(lst2)

s3 = s1 - s2

s4 = list(s3)

print(min(s4))
print(max(s4))

"""ps = [1,2,3,4,5]
ss = set(ps) <- 리스트를 집합으로 변환
tu = tuple(ps) <- 리스트를 튜플로 변환

**리스트의 중복을 제거하려면 집합으로 바꿔서 집합을 서로 빼기**

# 2025-05-13
"""

lst=[]
for i in range(10):
  a = int(input())
  b = a % 42
  lst.append(b)

ps1 = set(lst)
ps2 = list(ps1)

print(len(ps2))

N, M = map(int, input().split())
lst=[]
for i in range(1,N+1):
  lst.append(i)

for i in range(M):
  a, b = map(int, input().split())
  temp = lst[a-1:b]
  temp.reverse()
  lst[a-1:b] = temp


for i in range(N):
  print(lst[i], end=" ")

N = int(input())
lst1 = list(map(int, input().split()))
lst2 = []
m = max(lst1)
for i in range(N):
  lst2.append((lst1[i]/m*100))

avg =  (sum(lst2)/N)
print(avg)

S = input()
i = int(input())
print(S[i-1])

"""# 2025-05-14"""

N = input()
print(len(N))

T = int(input())

for i in range(T):
  N = input()
  print(N[0]+N[-1])

a = input()

print (ord(a))

"""아스키코드 변환법 ord(변수)"""

N = int(input())
lst = list(map(int, input()))
print(sum(lst))

S = input()
C = 'abcdefghijklmnopqrstuvwxyz'


for i in C:
  if i in S:
    print(S.index(i), end= ' ')
  else :
    print(-1, end=' ')

T = int(input())
for i in range(T):
  R, S = input().split()
  for i in range(len(S)):
    print(S[i] * int(R), end = '')
  print('')

S = input()

count = S.split()
print(len(count))

"""# 2025-05-15"""

a,b = input().split()

a = int(a[::-1])
b = int(b[::-1])

if a > b:
  print(a)
else:
  print(b)

code=['ABC','DEF','GHI','JKL','MNO','PQRS','TUV','WXYZ']
a = input()
k=0
for i in range(len(a)):
  for j in code:
    if a[i] in j:
      k += code.index(j)+3

print(k)

"""# 2025-05-19"""

while True:
  try :
    print(input())
  except EOFError:
    break

while True:
  num = list(map(int, input().split()))
  if sum(num) == 0:
    break

  max_num = max(num)
  num.remove(max_num)


  if num[0]**2 + num[1]**2 == max_num**2:
     print("right")
  else:
     print("wrong")

while True:
  n = input()
  if int(n) == 0:
    break
  else:
    if n == n[::-1]:
      print('yes')
    else:
      print('no')

data = [1,1,2,2,2,8]

num = list(map(int,input().split()))
x=0
lst2=[]
for i in range(6):
  x = data[i] - num[i]
  lst2.append(x)

for i in range(6):
  print(lst2[i], end=' ')

def factorial(n):
  num = 1
  for i in range(1,n+1):
    num *= i
  return num

T = int(input())

for i in range(T):
  N,M = map(int, input().split())
  k = factorial(M)//(factorial(N)*factorial(M-N))
  print(k)

lst=[64, 32, 16, 8, 4, 2, 1]
x = int(input())
count=0

for i in range(len(lst)):
  if x >= lst[i]:
    count+=1
    x-=lst[i]
  else:
    pass

print(count)

N = int(input())
score = [0] * N
lst=[]
for i in range(N):
  student = list(map(int, input().split()))
  lst.append(student)


for a in range(N):
  for b in range(N):
    if a == b:
      continue
    for c in range(5):
        if lst[a][c] == lst[b][c]:
            score[a] += 1
            break


print(score.index(max(score))+1)

#윤년 366일
#평년 365일
#1308번

def calc_day(y,m,d):
  lst1=[0,31,28,31,30,31,30,31,31,30,31,30,31]
  day = 0
  for i in range(1,y):
    day+=(365+is_leaf(i))

  for i in range(1,m):
    if i == 2 :
      day+= is_leaf(y)
    day += lst1[i]
  return day+d


def is_gg(dy, dm, dd, ty, tm, td):
    if dy-ty > 1000 or (dy-ty==1000 and (dm-tm > 0 or (dm-tm==0 and dd-td >= 0))):
        return True
    else:
        return False

def is_leaf(y):
  if y%400 == 0 or (y % 4 ==0 and y%100 !=0):
    return 1
  else:
    return 0



ty, tm, td = map(int, input().split())
dy, dm, dd = map(int, input().split())

today=0
dday=0

if is_gg(dy, dm, dd, ty, tm, td):
    print("gg")

else:
  today = calc_day(ty,tm,td)
  dday = calc_day(dy,dm,dd)
  print("D-%d" %(dday-today))

a,b,c = map(int,input().split())


for i in range(c):
  a = (a%b) * 10
  x = a//b

print(x)

"""# 2025-05-25"""

N = int(input())

count=0

for i in range(N):
  word = input()
  m = set()
  p = ''
  test=True

  for a in word:
    if a != p:
      if a in m:
        test=False
        break
      m.add(a)
    p = a

  if test:
    count+=1

print(count)

#25000

A,B,C= map(int,input().split())
S,V= map(int,input().split())
L = int(input())

need_level = (25000 - ((L*100)+(S*30*B)+(V*30*C)))

m=1

while (m*A) < need_level:
  m+=1
print(m+(S*30)+(V*30))

A, B, C = map(int, input().split())  # 이벤트, 수련관, 사우나 경험치
S, V = map(int, input().split())     # 수련관/사우나 입장권 개수
L = int(input())                     # 현재 레벨

need_exp = (250 - L) * 100
total_min = 0

# 1. 사우나부터 사용 (가장 많은 경험치)
for _ in range(V):
    if need_exp <= 0:
        break
    gain = C * 30
    need_exp -= gain
    total_min += 30

# 2. 수련관 사용
for _ in range(S):
    if need_exp <= 0:
        break
    gain = B * 30
    need_exp -= gain
    total_min += 30

# 3. 이벤트 맵으로 남은 경험치 채우기
if need_exp > 0:
    total_min += (need_exp + A - 1) // A  # 올림 나눗셈

print(total_min)

"""# 2025-05-26"""

n,m = map(int,input().split())
a=[]
b=[]
sum=[]

for i in range(n):
  k = list(map(int,input().split()))
  a.append(k)

for i in range(n):
  j = list(map(int,input().split()))
  b.append(j)




for i in range(n):
  for j in range(m):
    sum = a[i][j]+b[i][j]
    print(sum,end=' ')
  print()

n=int(input())
result = (((2**n)+1)**2)
print(result)





print(16%10%10%10)

T =  int(input())
for i in range(T):
  a,b=map(int,input().split())
  a = a%10
  if a == 1 or a == 5 or a == 6:
    print(a)
  elif a == 0:
    print(10)
  elif a == 4 or a == 9:
    b = b % 2
    if b == 1:
      print(a)
    else:
      print((a*a)%10)
  else:
    b = b % 4
    if b == 0:
      print((a**4)%10%10%10)
    else:
      print((a**b)%10%10%10)

color_data = ["black","brown","red","orange","yellow","green","blue","violet","grey","white"]
lst=[]
for i in range(3):
  color = input()
  N = color_data.index(color)
  lst.append(N)

c = 10**lst[2]

a = lst[0] * (10**(lst[2]+1))
b = lst[1] * c

print(a+b)

T = int(input())

if T == 1:
  a=int(input())
  print(a**2)

else:

  db = list(map(int,input().split()))

  db1 = set(db)
  db2 = list(sorted(db1))


  print(db2[0]*db2[-1])

name = input()
T = int(input())
lst_name=[]
lst_score=[]
L=0
O=0
V=0
E=0
for k in name:
  if k == 'L':
      L+=1
  elif k == 'O':
      O+=1
  elif k == 'V':
      V+=1
  elif k == 'E':
      E+=1
L1=L
O1=O
V1=V
E1=E

for i in range(T):
  n=input("")
  lst_name.append(n)
  for k in n:
    if k == 'L':
      L+=1
    elif k == 'O':
      O+=1
    elif k == 'V':
      V+=1
    elif k == 'E':
      E+=1


  score = ((L+O)*(L+V)*(L+E)*(O+V)*(O+E)*(V+E))%100
  lst_score.append(score)
  L=L1
  O=O1
  V=V1
  E=E1

max_score = max(lst_score)

max_names=[]
for i in range(len(lst_score)):
  if lst_score[i] == max_score:
    max_names.append(lst_name[i])

max_names = sorted(max_names)
print(max_names[0])



N = int(input())
size = list(map(int,input().split()))
T , P = map(int,input().split())
count=0
sum=0
for i in range(6):
  if size[i] % T == 0:
    count = size[i]//T
  else:
    count = size[i]//T + 1
  sum+=count



print(sum)
print(N//P, N%P)

def num(x):
  if x == 1:
    return False
  for i in range(2,x):
    if x % i  == 0:
      return False
  return True




T = int(input())

count=0
a = list(map(int,input().split()))

for i in range(T):
  if num(a[i]) == True:
    count+=1
  else:
    pass

print(count)

N = int(input())
lst=[]

for i in range(N):
  a = list(map(int,input().split()))
  lst.append(a)

lst.sort()

for i in range(N):
  print(lst[i][0],lst[i][1])

N = int(input())
lst=[]

for i in range(N):
  a = list(map(int,input().split()))
  a.reverse()
  lst.append(a)

lst.sort()

for i in range(N):
  print(lst[i][1],lst[i][0])

n = int(input())
cnt = 0
result = 666

while True:
  if '666' in str(result):
    cnt += 1
  if cnt == n:
    break
  result += 1

print(result)

L = int(input())
string = input()
answer = 0
M = 1234567891
r = 31

for i in range(L):
  cur = ord(string[i]) - 96
  answer += cur * (r**i)

print(answer%M)

#1
#2~7
#8~19
#20~37
#38~61
#62~92

#1-7-19-37-61
# 6 12 18 24
n = int(input())
a1 = 1
d = 6
room = 1
if n == 1:
  print(1)
else:
  while True:
    a1 += d
    room +=1
    if n <= a1 :
      print(room)
      break
    d += 6

N = int(input())
x = []
y = []
score = [1] * N
for i in range(N):
  a,b = map(int,input().split())
  x.append(a)
  y.append(b)

for i in range(N):
  for k in range(N):
    if x[i] < x[k] :
      if y[i] < y[k]:
        score[i]+=1


for i in range(N):
  print(score[i],end=' ')

N = int(input())
member_lst = []
for i in range(N):
  age,name = map(str, input().split())
  age = int(age)
  member_lst.append((age,name))

member_lst.sort(key = lambda x : x[0])

for i in member_lst:
  print(i[0], i[1])

N = int(input())
lst=[]

for i in range(1,N+1):
  a = int(input())
  if a == 0:
    lst.pop()

  else:
    lst.append(a)

print(sum(lst))

K , N = map(int,input().split())
data = []

for i in range(K):
  line = int(input())
  data.append(line)

start = 1
end = max(data)
result = 0

while start <= end:
  cnt = 0
  mid = (start + end) // 2

  for i in data:
    cnt += (i // mid)

  if cnt >= N :
    result = mid
    start = mid + 1
  else:
    end = mid - 1

print(result)

a = int(input())

for i in range(a):
  N, M = map(int,input().split())
  data = list(map(int,input().split()))

  result = 1
  while data:
    if data[0] < max(data):
      data.append(data.pop(0))

    else:
      if M == 0 :
        break

      data.pop(0)
      result +=1

    if M > 0:

      M = M - 1
    else:
      M = len(data) - 1

  print(result)

n = int(input())

if (n % 5 ) == 0 :
  print(n//5)
else:
  p = 0
  while n > 0:
    p+=1
    n-=3
    if n % 5 == 0:
      p += n//5
      print(p)
      break
    elif n == 0:
      print(p)
      break
    elif n == 1 or n == 2:
      print(-1)
      break

n = int(input())
lst=[]
sum = 0

count = dict()
for i in range(n):
  x=int(input())
  lst.append(x)
  sum+=x

  if x not in count:
    count[x] = 1
  else:
    count[x]+=1

lst.sort()

print(round(sum/n))

print(lst[n//2])
number=[]
freq = max(count.values())
for key, value in count.items():
  if value == freq:
    number.append(key)

if len(number) == 1:
  print(number[0])
else:
  print(sorted(number)[1])



print(lst[-1]-lst[0])

import sys

input = sys.stdin.readline

n = int(input().strip())
data = []
for i in range(n):
  x = int(input())
  data.append(x)

data.sort()

for i in data:
  print(i)

