class Solution {
public:
    int getSum(int a, int b) {
        if (!b) return a;
        return getSum(a^b, (a&b) << 1);
    }
};
