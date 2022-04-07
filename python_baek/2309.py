# 2309.py 일곱 난쟁이

n = [int(input()) for _ in range(9)]
total = sum(n)

for i in range(9):
    for j in range(i+1, 9):
        # 리스트에서 remove사용시 인덱스가 바뀜을 주의하기
        if total - (n[i] + n[j]) == 100:
            num1, num2 = n[i], n[j]
            n.remove(num1)
            n.remove(num2)
            n.sort()

            for i in range(len(n)):
                print(n[i])
            break

    if len(n) < 9:
        break