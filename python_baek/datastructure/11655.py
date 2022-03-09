# 11655.py ROT13
# https://www.acmicpc.net/problem/11655

S = input()
ans = ''

for s in S:
    if s.isalpha():
        if s.isupper():
            ans += chr((ord(s) - ord('A') + 13) % 26 + ord('A'))
        else:
            ans += chr((ord(s) - ord('a')+ 13) % 26 + ord('a'))
    else:
        ans += s

print(''.join(ans))