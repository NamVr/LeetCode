class Solution {
public:
    int maximumSwap(int num) {
        string str = to_string(num);

        // trackers
        int maxdigit = -1, maxidx = -1;
        int leftidx = -1, rightidx = -1;

        for (int i = str.size() - 1; i >= 0; i--) {
            if (str[i] > maxdigit) {
                maxdigit = str[i];
                maxidx = i;
                continue;
            }

            if (str[i] < maxdigit) {
                leftidx = i;
                rightidx = maxidx;
            }
        }

        if (leftidx == -1) return num;
        swap(str[leftidx], str[rightidx]);
        return stoi(str);
    }
};
