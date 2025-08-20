class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]: 
        res = [] # keep only positive values.

        for a in asteroids:
            # if the asteroid is coming towards, pop the stack,
            while res and a < 0 < res[-1]:

                # if its bigger, demolish the smaller value.
                if abs(a) > res[-1]:
                    res.pop()
                    continue # to the next stack element.
                
                elif abs(a) == res[-1]:
                    res.pop() # demolish both.
                
                break
            else:
                res.append(a)
        

        return res
