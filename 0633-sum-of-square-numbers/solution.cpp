class Solution {
public:
    bool judgeSquareSum(int c) {
        int l = 0 , r = sqrt(c);

        while (l <= r) {
            long int sum = pow(l,2) + pow(r,2);

            if (sum == c) return true;

            if (sum > c) r--;
            else l++;
        }

        return false;
    }
};
