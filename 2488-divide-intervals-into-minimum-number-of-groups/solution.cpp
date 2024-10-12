class Solution {
public:
    int minGroups(vector<vector<int>>& intervals) {
        vector<int> start, end;

        for (const auto& interval : intervals) {
            start.push_back(interval[0]);
            end.push_back(interval[1]);
        }

        sort(start.begin(), start.end());
        sort(end.begin(), end.end());

        int ep = 0, group = 0;

        for (int s : start) {
            if (s > end[ep]) ep++;
            else group++;
        }

        return group;
    }
};
