class Solution:
    def numSteps(self, s: str) -> int:
        steps = 0 # number of steps
        carry = 0 # carry after addition of odd bit

        for i in reversed(range(1, len(s))):
            bit = ord(s[i]) & 1 # take the most right bit in unicode and check odd/even
            
            steps += 1 + (bit ^ carry)
            carry |= bit
        
        return steps + carry
