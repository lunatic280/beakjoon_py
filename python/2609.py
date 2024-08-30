import sys

a, b = map(int, sys.stdin.readline().split())

x = 0
if a > b:
    x = a
else:
    x = b
for i in range(1, x+1):
    if (a % i == 0) and (b % i == 0):
        result1 = i

result3 = a * b // result1

print(result1)
print(result3)
