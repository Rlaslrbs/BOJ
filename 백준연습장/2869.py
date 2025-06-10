import math
A,B,V = map(int,input().split())

# 1 2 / 2 1/ 3 1 / 4 1

day = (V - B) / (A - B)

print(math.ceil(day))