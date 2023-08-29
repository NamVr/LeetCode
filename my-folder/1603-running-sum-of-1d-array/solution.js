/**
 * @param {number[]} nums
 * @return {number[]}
 */
var runningSum = function(nums) {
    const arr = [];
    let n = 0;

    for (let i = 0; i < nums.length; i++) {
        n = n + nums[i]
        arr.push(n)
    }
    
    return arr;
};
