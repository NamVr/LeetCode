class Solution {
public:
    string gcdOfStrings(string str1, string str2) {
        // if concat of strings is equal then they have a gcd
        if (str1+str2 != str2+str1) return "";

        // find gcd of their size and return strings
        return str1.substr(0,gcd(size(str1),size(str2)));
    }
};
