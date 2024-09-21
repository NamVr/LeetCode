/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[]}
 */
var twoSum = function(nums, target) {
    const arr = [];
    upper:
    for (let i = 0; i < nums.length; i++) {
        for (let n = 0; n < nums.length; n++) {
            if (n==i) continue;
            if (target == nums[i] + nums[n]) {
            arr.push(i, n);
            break upper;
        }
        
        }
    }

    return arr;
};
