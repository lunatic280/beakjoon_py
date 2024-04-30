import sys
input = sys.stdin.readline
def quick(arr):
   
   if len(arr) <= 1:
      return arr
   else:
      pivot = arr[0][0]
      right_sort = []
      left_sort = []
      equal = []

      for i in range(len(arr)):
         if arr[i][0] < pivot:
            left_sort.append(arr[i])
         elif arr[i][0] > pivot:
            right_sort.append(arr[i])
         else:
            equal.append(arr[i])
    
         
   return quick(left_sort) + equal_quick_sort(equal) + quick(right_sort)

def equal_quick_sort(equal):
   if len(equal) <= 1:
      return equal
   else:
      pivot = equal[0][1]
      right_sort = []
      left_sort = []
      equal_sort = []
    

   for i in range(len(equal)):
      if equal[i][1] < pivot:
        left_sort.append(equal[i])
      elif equal[i][1] > pivot:
        right_sort.append(equal[i])
      else:
        equal_sort.append(equal[i])
   return equal_quick_sort(left_sort) + equal_sort + equal_quick_sort(right_sort)

a = int(input())
arr = []
for i in range(a):
   input1 = list(map(int, input().split()))
   arr.append(input1)
result = quick(arr)
for x, y in result:
   print(x, y)



