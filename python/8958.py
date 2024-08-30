a = int(input())
arr_test = []
for i in range(a):
    arr = input()
    arr_test.append(arr)

for arr in arr_test:
    list(arr)
    plus = 1
    count = 0
    for i in arr:
        if i == "O":
            count += plus
            plus += 1
        else:
            plus = 1
    print(count)


