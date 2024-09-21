/**
 * @param {number[][]} accounts
 * @return {number}
 */
var maximumWealth = function(accounts) {
    let max = 0;
    for (let customer = 0; customer < accounts.length; customer++) {
        
        let x = accounts[customer].reduce((acc, cv) => acc + cv);
        max = Math.max(max, x);
    }

    return max;
};
