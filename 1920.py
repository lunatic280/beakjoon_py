n = int(input())
arr_n = list(map(int, input().split()))
m = int(input())
arr_m = list(map(int, input().split()))
result = []

for i in range(m):
    if arr_m[i] in arr_n:
        result.append(1)
    else:
        result.append(0)

print(result)
