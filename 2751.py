import sys

'''def quick_sort(arr1):
    if len(arr1) <= 1:
        return arr1
    else:
        pivot = arr1[0]
        left_arr = []
        right_arr = []
        equal__arr = []

        for i in arr1:
            if i < pivot:
                left_arr.append(i)
            elif i > pivot:
                right_arr.append(i)
            else:
                equal__arr.append(i)
        left_quick_sort = quick_sort(left_arr)
        right_quick_sort = quick_sort(right_arr)
        return left_quick_sort + equal__arr + right_quick_sort
        '''
t = int(sys.stdin.readline())

arr1 = []
for i in range(t):
    a = int(sys.stdin.readline())
    arr1.append(a)

arr1.sort(reverse=False)
for i in arr1:
    print(i)
#result = quick_sort(arr1)

'''for i in result:
    print(i)'''


