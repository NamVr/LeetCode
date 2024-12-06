class Solution {
public:
    int maxCount(vector<int>& banned, int n, int maxSum) {
        unordered_set<int> s(banned.begin(), banned.end());

        int res = 0, sum = 0;

        for (int i = 1; i <= n; i++) {
            if (s.count(i)) continue;

            if (sum + i > maxSum) break;

            sum += i;
            res++;
        }


        return res;
    }
};
