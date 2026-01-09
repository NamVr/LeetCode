class Solution:
    def canMeasureWater(self, x: int, y: int, z: int) -> bool:
        # If z is 0, we don't need to do anything
        if z == 0:
            return True
        # If total capacity is less than z, impossible to measure z
        if x + y < z:
            return False
        # If one of the jugs has zero capacity, then we can only measure z if z equals the other jug's capacity
        if x == 0 or y == 0:
            return z == x or z == y

        # Helper function to compute gcd
        def gcd(a, b):
            # Euclidean algorithm
            while b:
                a, b = b, a % b
            return a

        g = gcd(x, y)
        # z must be a multiple of the GCD of x and y
        return z % g == 0
