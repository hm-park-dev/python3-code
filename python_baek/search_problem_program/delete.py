# 번호 입력 시 특정 번호를 제거하는 프로그램

del_num = input('Input delete problem number >> ')
f = open("./python_baek/search_problem_program/problem_list.txt", 'r', encoding='utf-8')
problems = list()
del_state = False

line = f.readline()
while line:
    code, str = line.strip().split(',')
    if code == del_num:
        print(f'Delete: No. {code} {str}')
        del_state = True
    else:    
        problems.append(line)
    line = f.readline()
f.close()

if del_state == False:
    print(f'Can\'t find No. {del_num}')
else:
    f = open("./python_baek/search_problem_program/problem_list.txt", 'w', encoding='utf-8')
    for problem in problems:
        f.write(problem)
    f.close()