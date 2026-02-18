class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        b = bin(n)[2:]

        last_state = "1" if b[0] == "0" else "0"

        for c in b:
            if c == last_state:
                return False
            
            last_state = c
        
        return True
