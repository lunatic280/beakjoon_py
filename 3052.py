arr = []
for i in range(10):
    a = int(input())
    arr.append(a)

result = []
for i in arr:
    s = i % 42
    result.append(s)
result1 = []
for i in result:
    if i not in result1:
        result1.append(i)
print(len(result1))