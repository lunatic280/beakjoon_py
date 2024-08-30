a = int(input())

arr = []

for i in range(a):
    a, b = map(int, input().split())
    arr.append((a, b))
arr.sort()

for x, y in arr:
    print(x, y)