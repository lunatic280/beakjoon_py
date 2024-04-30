import sys
deque1 = []
def push_front(x):
    deque1.insert(0, x)

def push_back(x):
    deque1.append(x)

def pop_front():
    if len(deque1) == 0:
        print(-1)
    else:
        print(deque1[0])
        del deque1[0]

def pop_back():
    if len(deque1) == 0:
        print(-1)
    else:
        print(deque1[len(deque1) - 1])
        deque1.pop()

def size():
    print(len(deque1))

def empty():
    if len(deque1) == 0:
        print(1)
    else:
        print(0)

def front():
    if len(deque1) == 0:
        print(-1)
    else:
        print(deque1[0])

def back():
    if len(deque1) == 0:
        print(-1)
    else:
        print(deque1[len(deque1) - 1])

a = int(input())
for i in range(a):
    input1 = []
    input1 = list(map(str, sys.stdin.readline().split()))
    if input1[0] == "push_front":
        push_front(input1[1])
    elif input1[0] == "push_back":
        push_back(input1[1])
    elif input1[0] == "pop_front":
        pop_front()
    elif input1[0] == "pop_back":
        pop_back()
    elif input1[0] == "size":
        size()
    elif input1[0] == "empty":
        empty()
    elif input1[0] == "front":
        front()
    elif input1[0] == "back":
        back()




