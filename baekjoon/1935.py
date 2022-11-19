# 1935.py 후위표기식

N = int(input())
post = list(input())
stack = list()
nums = list()

for _ in range(N):
    nums.append(int(input()))

# postfix -> infix
for p in post:
    if 'A' <= p <= 'Z':
        stack.append(nums[ord(p) - ord('A')])
    else:
        operand_2 = stack.pop()
        operand_1 = stack.pop()

        if p == '+':
            stack.append(operand_1 + operand_2)
        elif p == '-':
            stack.append(operand_1 - operand_2)
        elif p == '*':
            stack.append(operand_1 * operand_2)
        elif p == '/':
            stack.append(operand_1 / operand_2)

ans = stack.pop()
# 소수점 둘째 자리까지
print(f"{ans:0.2f}")