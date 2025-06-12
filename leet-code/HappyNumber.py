class Solution:
    def isHappy(self, n: int) -> bool:
        if n < 10 and n != 1:
            return False
        
        while True:
            total = sum(int(digit) ** 2 for digit in str(n))
            n = total
            if total == 1:
                return True
