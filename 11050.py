import sys
def pack(num):
   sum1 = 1
   for i in range(2, num + 1):
       sum1 = sum1 * i
   return sum1

n, k = map(int,sys.stdin.readline().split())
if k < 0:
    print(0)
elif k > n:
    print(0)
else:
    result = pack(n) / (pack(k) * pack(n - k))
    print(int(result))
