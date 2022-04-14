# 랜덤으로 문제를 읽어오는 프로그램
f = open(".\python_baek\search_problem_program\problem_list.txt", 'r', encoding='utf-8')
problems = list()

while True:
    code, str = f.readline().split(',')
    print(code, str)

f.close()