# 10845.py 큐

# 시간초과 -> sys.stdin.readline()이 아닌 input()을 사용했을 때 나타남

import sys

queue = list()
for _ in range(int(input())):
    command = sys.stdin.readline().split()

    if command[0] == "push":
        queue.append(command[1])
    elif command[0] == "pop":
        if queue:
            print(queue.pop(0))
        else: print(-1)
    elif command[0] == "size":
        print(len(queue))
    elif command[0] == "empty":
        if queue:
            print(0)
        else: print(1)
    elif command[0] == "front":
        if queue:
            print(queue[0])
        else: print(-1)
    elif command[0] == "back":
        if queue:
            print(queue[-1])
        else: print(-1)