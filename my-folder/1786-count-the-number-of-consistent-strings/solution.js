/**
 * @param {string} allowed
 * @param {string[]} words
 * @return {number}
 */
var countConsistentStrings = function(allowed, words) {
    let count = 0;
    for (let word of words) {
        for (const letter of allowed) {
            word = word.replaceAll(letter, "");
        }
        if (!word) count++;
    }

    return count;
};
