
import sys
input = sys.stdin.readline
n, m  = map(int, input().split())

a = set()
b = set()

for i in range(n):
    name = input().strip()
    a.add(name)

for i in range(m):
    name = input().strip()
    b.add(name)

print(len(sorted(list(a&b))))
for i in sorted(list(a&b)):
    print(i)

        


