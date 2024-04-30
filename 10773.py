a = int(input())
arr = []
for i in range(a):
    b = int(input())
    if b == 0:
        arr.pop()
    else:
        arr.append(b)
result = 0
for i in arr:
    result += i

print(result)
