#import sys
#sys.stdin = open("input.txt", "r")

match = 'abcdefghijklmnopqrstuvwxyz'

T = int(input())
ind = 1
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    # ///////////////////////////////////////////////////////////////////////////////////
    str = input()
    ans = 0
    for i in range(len(str)):
        if str[i] == match[i]:
            ans += 1
        else:
            break
    print(f'#{ind} {ans}')
    ind += 1
    # ///////////////////////////////////////////////////////////////////////////////////
