def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[0]
        left = []
        right = []
        equal = []

        for element_count in range(len(arr)):
            if len(arr[element_count]) < len(pivot):
                left.append(arr[element_count])
            elif len(arr[element_count]) > len(pivot):
                right.append(arr[element_count])
            else:
                equal.append(arr[element_count]) 
        
        sorted_left = quick_sort(left)
        sorted_right = quick_sort(right)
        equal.sort()

        return sorted_left + equal + sorted_right
    
a = int(input())
arr = []
for i in range(a):
    str1 = input()
    if str1 not in arr:
        arr.append(str1)
            
result = quick_sort(arr)
for word in result:
    print(word)