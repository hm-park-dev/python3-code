# 랜덤으로 문제를 읽어오는 프로그램
import random

f = open("./python_baek/search_problem_program/problem_list.txt", 'r', encoding='utf-8')
problems = list()

line = f.readline().strip()
while line:
    code, str = line.split(',')
    problems.append([code, str])
    line = f.readline().strip()
f.close()

length = len(problems)
ret = problems[random.randrange(length)]
print(f'Problem: No. {ret[0]} {ret[1]}')