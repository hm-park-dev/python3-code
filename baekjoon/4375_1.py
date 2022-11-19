# 4375_1.py
# 29200 KB 200 ms
import sys
import time

class Solution:
    def get_answer(self, n: int) -> int:
        num = 0
        while True:
            num = num*10 + 1
            if num%n == 0:
                # print(num)
                break
        return len(str(num))



if __name__ == '__main__':
    s = Solution()
    lines = sys.stdin.readlines()

    for line in lines:
        # start = time.time()
        n = int(line)
        print(s.get_answer(n))
        # a = time.time() - start
        # print(f"{a} ms")