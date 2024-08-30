n = int(input())

arr = list(map(int, input().split()))
max_num = arr[0]
min_num = arr[0]

for i in range(1, n):
    if max_num <= arr[i]:
        max_num = arr[i]

for i in range(1, n):
    if min_num >= arr[i]:
        min_num = arr[i]

print(min_num, max_num)