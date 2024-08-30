a = int(input())
arr = int(input())
arr = list(map(int, str(arr)))
sum = 0
for i in arr:
    sum  = sum +int(i)

print(sum)