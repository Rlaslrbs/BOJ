
import sys
input = sys.stdin.readline

N = int(input())

result = []
paper = [list(map(int, input().split())) for _ in range(N)]

def solution(x,y,t):
    color = paper[x][y]
    for i in range(x,x+t):
        for j in range(y,y+t):
            if color != paper[i][j]:
                solution(x+t//2,y,t//2)
                solution(x+t//2,y+t//2,t//2)
                solution(x,y+t//2,t//2)
                solution(x,y,t//2)
                return


    if color == 0:
        result.append(0)
    if color == 1:
        result.append(1)


solution(0,0,N)
print(result.count(0))
print(result.count(1))
