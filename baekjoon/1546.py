# 1546.py 평균

N = int(input())
scores = list(map(int, input().split()))
max_value = max(scores)
previous_sum = sum(scores)

print(previous_sum * 100 / max_value / N)