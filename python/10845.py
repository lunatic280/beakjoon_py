import sys
arr = []

def push(x):
    arr.append(x)

def pop():
    if len(arr) == 0:
        print(-1)

    else:
        print(arr[0])
        del arr[0]

def size():
    print(len(arr))

def empty():
    if len(arr) == 0:
        print(1)
    else:
        print(0)

def front():
    if len(arr) != 0:
        print(arr[0])
    else:
        print(-1)

def back():
    if len(arr) == 0:
        print(-1)
    else:
        print(arr[len(arr) - 1])


a = int(sys.stdin.readline())
for i in range(a):
    input1 = sys.stdin.readline().split()
    if input1[0] == "push":
        push(input1[1])
    elif input1[0] == "pop":
        pop()
    elif input1[0] == "size":
        size()
    elif input1[0] == "empty":
        empty()
    elif input1[0] == "front":
        front()
    elif input1[0] == "back":
        back()

