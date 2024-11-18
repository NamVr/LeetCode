class Solution {
public:
    vector<int> decrypt(vector<int>& code, int k) {
        int n = code.size();
        vector<int> res(n, 0);

        if (k == 0) return res;

        for (int i = 0; i < n; i++) {
            if (k > 0) {
                for (int j = i + 1; j < i + k + 1; j++) {
                    res[i] += code[j % code.size()];
                }
            } else {
                for (int j = i - abs(k); j < i; j++) {
                    res[i] += code[(j + code.size()) % code.size()];
                }
            }
        }

        return res;
    }
};
