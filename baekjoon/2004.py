# 2004.py 조합 0의 개수
# https://www.acmicpc.net/problem/2004

# factorial DP or 재귀: 매우 느림 + 메모리 터짐
# 수학적인 방법을 사용해야 함

# 10의 개수 -> 10 = 2 * 5 가 얼마나 곱해졌는가?
# 2와 5의 개수를 알아야 함

def count_num(target, num):
    count = 0
    while target:
        target = target // num
        count = count + target
    return count

n, m = map(int, input().split())

n_2 = count_num(n, 2)
n_5 = count_num(n, 5)

r_2 = count_num(n-m, 2)
r_5 = count_num(n-m, 5)

m_2 = count_num(m, 2)
m_5 = count_num(m, 5)

count_5 = n_5 - r_5 - m_5
count_2 = n_2 - r_2 - m_2

print(min(count_5, count_2))