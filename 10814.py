
def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    
    pivot = arr[0][0]
    left_list = []
    right_list = []
    equal_list = []
    for i in range(len(arr)):
        if arr[i][0] < pivot:
            left_list.append(arr[i])
        elif arr[i][0] > pivot:
            right_list.append(arr[i])
        else:
            equal_list.append(arr[i])
    sort_left = quick_sort(left_list)
    sort_right = quick_sort(right_list)

    return sort_left + equal_list + sort_right
    
a = int(input())
arr = []
for i in range(a):
    age_name = list(input().split())
    arr.append(age_name)

result = quick_sort(arr)

for age, name in result:
    print(age, name)