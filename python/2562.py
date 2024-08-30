arr = [] 
max_num = 0
count = 0
for i in range(9):
    arr.append(int(input()))
    if arr[i] >= max_num:
        max_num = arr[i]
        count = i+1
print(max_num)
print(count)
