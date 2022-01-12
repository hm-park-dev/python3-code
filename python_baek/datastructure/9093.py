# 9093.py 단어 뒤집기

for _ in range(int(input())):
    sen = input().split()
    for i in range(len(sen)):
        print(''.join(list(reversed(sen[i]))), end=' ')
    print()