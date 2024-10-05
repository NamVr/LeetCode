class Solution {
public:
    bool isValidSudoku(vector<vector<char>>& board) {
        unordered_map<int,set<char>> cols;
        unordered_map<int,set<char>> rows;
        unordered_map<int,set<char>> sub;

        for (int r = 0; r < 9; r++) {
            for (int c = 0; c < 9; c++) {
                int val = board[r][c];
                if (val == '.') continue;

                int x = (r/3)*3 + (c/3);
                if ((rows[r].find(val) != rows[r].end()) || (cols[c].find(val) != cols[c].end()) || (sub[x].find(val) != sub[x].end())) {
                    return false;
                }

                // update hashmap
                rows[r].insert(val);
                cols[c].insert(val);
                sub[x].insert(val);
            }
        }

        return true;
    }
};
