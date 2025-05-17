class Solution:
    def sortColors(self, nums: List[int]) -> None:
        # Use a counter for 2 pass solution, but it's boring.
        # Let's do something innovative instead.
        
        # Dutch National Flag Algorithm.
        low = mid = 0
        high = len(nums) - 1

        while mid <= high:
            if nums[mid] == 0: # color 0
                nums[low], nums[mid] = nums[mid], nums[low]
                low += 1 # since color 0 is added, both pointers
                mid += 1 # low and mid is increment.
            elif nums[mid] == 1: # color 1
                mid += 1 # only color 1 is added, increment mid.
            else:
                nums[mid], nums[high] = nums[high], nums[mid]
                high -= 1 # shift boundary for color 2.
