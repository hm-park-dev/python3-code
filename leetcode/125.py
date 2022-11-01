# 1 Valid Palindrome

import collections
from typing import Deque
import re


class Palindrome:
    def is_palindrome_list(self, s: str) -> bool:
        strs = []
        for char in s:
            if char.isalnum():
                strs.append(char.lower())
        
        while len(strs) > 1:
            if strs.pop(0) != strs.pop():
                return False
        return True
    
    def is_palindrome_deque(self, s: str) -> bool:
        strs: Deque = collections.deque()
        for char in s:
            if char.isalnum():
                strs.append(char.lower())
        
        while len(strs) > 1:
            if strs.popleft() != strs.pop():
                return False
        return True

    def is_palindrome_slicing(self, s: str) -> bool:
        s = s.lower()
        # 정규식 사용
        s = re.sub('[^a-z0-9]', '', s)
        return s == s[::-1]


if __name__ == '__main__':
    p = Palindrome()
    strs = "A man, a plan, a canal: Panama"
    a1 = p.is_palindrome_list(strs)
    print(a1)
    a2 = p.is_palindrome_deque(strs)
    print(a2)
    a3 = p.is_palindrome_slicing(strs)
    print(a3)