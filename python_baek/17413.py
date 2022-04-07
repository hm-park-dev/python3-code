# 17413.py 단어 뒤집기2

str = input()
ans = list()
stack = list()
flag = 0

for c in str:
    # 태그 시작 / 공백
    if c == '<':
        # 기존 단어 뒤집어서 넣기
        while stack:
            ans.append(stack.pop())
        ans.append(c)
        flag = 1
    elif c == '>':
        ans.append(c)
        flag = 0
    elif flag == 1:
        ans.append(c)
    elif c == ' ':
        # 기존 단어 뒤집어서 넣기
        while stack:
            ans.append(stack.pop())
        ans.append(c)        
    else:
        stack.append(c)

while stack:
    ans.append(stack.pop())

print(''.join(ans))