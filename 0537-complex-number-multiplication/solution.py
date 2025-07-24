class Solution:
    def complexNumberMultiply(self, num1: str, num2: str) -> str:
        a1, b1 = num1.split("+") # a + b * i
        a2, b2 = num2.split("+")

        b1 = b1.replace("i", "")
        b2 = b2.replace("i", "")

        # Simulation
        # a1 * a2 = real part
        # a1 * b2 = img
        # b1 * a2 = img
        # b1 * b2 = i^2 img

        x = int(a1)*int(a2) # real part x
        y = int(a1)*int(b2) + int(b1)*int(a2) # img part step 2,3
        z = int(b1)*int(b2)*-1 # i^2 img part

        x += z

        return str(x) + "+" + str(y) + "i"
