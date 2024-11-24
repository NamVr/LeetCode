class Solution {
public:
    long long maxMatrixSum(vector<vector<int>>& matrix) {
        // count number of negative signs
        long long neg_cnt = 0, ans = 0, size = matrix.size(), minn = 1000000;

        // keep track of absolute sum of all values.
        for (int i = 0; i < size; ++i)
            for (int j = 0; j < size; ++j) {
                ans += abs(matrix[i][j]);

                // check if the given element is negative
                if (matrix[i][j] < 0)
                    neg_cnt++;

                // keep track of the most minimum value absolute
                minn = minn < abs(matrix[i][j])? minn: abs(matrix[i][j]);
            }

        // if negative signs are even, answer is sum of all elements
        if (neg_cnt % 2 == 0)
            return ans;

        // otherwise, the most minimum value is subtracted (2x)
        else 
            return ans - 2*minn;
    }
};
