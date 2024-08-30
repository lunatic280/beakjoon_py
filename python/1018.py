rows, cols = map(int, input().split())
arr_2d1 = []
arr_2d2 = []
for i in range(rows):
    row = list(map(int, input().split()))
    arr_2d1.append(row)

for i in range(rows):
    row = list(map(int, input().split()))
    arr_2d2.append(row)

sum_2d = []
for j in range(rows):
    
    for i in range(cols):
        sum_2d[j][i] = arr_2d1[j][i] + arr_2d2[j][i]

for row in sum_2d:
    print(*row)


