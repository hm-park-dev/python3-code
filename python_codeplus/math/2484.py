# 2484.py 주사위 네개
import sys

if __name__ == '__main__':
    max = 0
    ret = 0

    n = int(sys.stdin.readline())
    for _ in range(n):
        nums = sorted(list(map(int, sys.stdin.readline().split())))

        # set은 중복되는 숫자가 없는 점을 이용한다
        if len(set(nums)) == 1:
            ret = 50000 + nums[0] * 5000
        elif len(set(nums)) == 2:
            if nums[1] == nums[2]:
                ret = 10000 + 1000 * nums[1]
            else:
                ret = 2000 + (nums[1] + nums[2]) * 500
        elif len(set(nums)) == 4:
            ret = nums[-1] * 100
        else:
            for i in range(3):
                if nums[i] == nums[i+1]:
                    ret = 1000 + nums[i] * 100
                    break
    
        if max < ret:
            max = ret

    print(max)