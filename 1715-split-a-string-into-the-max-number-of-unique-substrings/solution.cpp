class Solution {
public:
    int maxUniqueSplit(string s) {
        unordered_set<string> seen;
        return backtrack(0, s, seen);
    }

private:
    int backtrack(int start, const string& s, unordered_set<string>& seen) {
        if (start == s.size()) return 0;

        int M = 0;

        for (int end = start + 1; end <= s.size(); end++) {
            string sub = s.substr(start, end-start);
            
            if (seen.find(sub) == seen.end()) {
                seen.insert(sub);
                M = max(M, 1+backtrack(end,s,seen));
                seen.erase(sub);
            }
        }

        return M;
    }
};
