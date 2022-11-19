# 10828.py 스택
import sys

N = int(input())
end = 0

def push_s(stack: list, n: int):
    global end
    stack.append(n)
    end += 1


def pop_s(stack: list) -> int:
    global end
    if end == 0:
        return -1
    end -= 1
    return stack.pop()

def size_s(stack: list) -> int:
    return len(stack)

def empty_s(stack: list) -> int:
    if len(stack) == 0:
        return 1
    return 0

def top_s(stack: list) -> int:
    global end
    if end == 0:
        return -1
    return stack[end-1]

stack = list()
for _ in range(N):
    command = sys.stdin.readline().split()

    if command[0] == 'push':
        push_s(stack, command[1])
    elif command[0] == 'pop':
        print(pop_s(stack))
    elif command[0] == 'size':
        print(size_s(stack))
    elif command[0] == 'empty':
        print(empty_s(stack))
    elif command[0] == 'top':
        print(top_s(stack))