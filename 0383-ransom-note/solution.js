/**
 * @param {string} ransomNote
 * @param {string} magazine
 * @return {boolean}
 */
var canConstruct = function(ransomNote, magazine) {
    for (const c of magazine) {
        ransomNote = ransomNote.replace(c, "");
    }

    return !ransomNote;
};
