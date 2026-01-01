class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        carry = 1
        for i in reversed(range(len(digits))):
            s = digits[i] + carry
            digits[i] = s % 10
            carry = s // 10
        if carry:
            digits = [1] + digits
        return digits

