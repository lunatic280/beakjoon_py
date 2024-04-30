result = []
while True:
    arr = input()
    if arr == '0':
        break
    list_arr = list(arr)
    
    reverse_arr = []
    for i in range(len(list_arr) -1, -1, -1):
        reverse_arr.append(list_arr[i])
    count = 1
    for i in range(len(arr)):
        if arr[i] == reverse_arr[i]:
            count = 1
        else:
            count = 0
            break
    if count == 1:
        result.append("yes")
    else:
        result.append("no")

for i in result:
    print(i)