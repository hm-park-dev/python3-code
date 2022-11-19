# 1918.py 후위 표기식
# https://www.acmicpc.net/problem/1918

infix = list(input())

operator = list()
ans = ''

for i in infix :
    if i.isalpha():
        ans += i
    elif i == '(':
        operator.append(i)
    elif i == '*' or i == '/':
        while operator and (operator[-1] == '*' or operator[-1] == '/'):
            ans += operator.pop()
        operator.append(i)
    elif i == '+' or i == '-':
        while operator and operator[-1] != '(':
            ans += operator.pop()
        operator.append(i)
    elif i == ')':
        while operator and operator[-1] != '(':
            ans += operator.pop()
        operator.pop() ## ( 반환

while operator:
    ans += operator.pop()

print(ans)