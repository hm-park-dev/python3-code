# 랜덤으로 문제를 읽어오는 프로그램
import random

f = open("C:/Users/박해미/Desktop/Project/python3-code/python_baek/search_problem_program/problem_list.txt", 'r', encoding='utf-8')
problems = list()

line = f.readline().strip()
while line:
    code, str = line.split(',')
    problems.append([code, str])
    line = f.readline().strip()
f.close()

length = len(problems)
ret = problems[random.randrange(length)]
print(f'이번에 풀 문제는 {ret[0]}번 {ret[1]}')