# 10820.py 문자열 분석

def solution(str: list):
    upper = 0
    lower = 0
    nums = 0
    blank = 0

    for s in str:
        if s.isalpha():
            if s.isupper(): upper += 1
            else: lower += 1
        elif s.isdigit(): nums += 1
        else: blank += 1
    
    return print(lower, upper, nums, blank)

while True:
    try:
        solution(list(input()))
    except:    break