class Solution {
public:
    long long pickGifts(vector<int>& gifts, int k) {
        priority_queue<int> h(gifts.begin(), gifts.end());

        for (int i = 0; i < k; i++) {
            int maxElement = h.top();
            h.pop();

            h.push(sqrt(maxElement)); // heapify
        }

        long long res = 0;
        while (!h.empty()) {
            res += h.top();
            h.pop();
        }

        return res;
    }
};
