class Solution {
public:
    vector<int> lexicalOrder(int n) {
        vector<int> arr;
        int current = 1; // first element to push is 1

        for (int i = 0; i < n; i++) {
            // Use DFS
            arr.push_back(current);

            if (current * 10 <= n) {
                current *= 10;
            } else {
                // depth reached, reverse
                while (current % 10 == 9 || current + 1 > n) {
                    current /= 10;
                }
                ++current;
            }
        }
        return arr;
    }
};
