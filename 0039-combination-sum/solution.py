class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []

        # i -> current pointer, tells which of the candidates which we are still allowed to use for combinations
        # cur -> arr[] keeps the current combination of backtracking (eg: [2,2...])
        # total -> keeps the track of total of the current combination to check base cases.
        def dfs(i, cur, total):
            # BASE CASE: If total == target, append this result.
            if total == target:
                res.append(cur.copy())
                return
            
            # BASE CASE 2: If total > target or i is out of bounds, combination is impossible to find
            if i >= len(candidates) or total > target:
                return
            
            # Recursive steps: decision tree.
            # Start with i pointer, either pick up the number or dont.

            # Decision 1: Pick up the number, update the total.
            cur.append(candidates[i])
            dfs(i, cur, total + candidates[i])
            cur.pop() # clean up for next steps

            # Decision 2: Never pick up this number, move on to next pointer.
            dfs(i+1, cur, total)
        
        dfs(0, [], 0)

        return res
