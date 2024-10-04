class Solution {
public:
    long long dividePlayers(vector<int>& skill) {
        // sort the array
        sort(skill.begin(), skill.end());

        // two pointer approach
        int n = skill.size();

        // final answer is long long int
        long long ans = 0;

        // get an optimal target
        int target = skill[0] + skill[n-1];

        for (int i = 0; i < n/2; i++) {
            // return -1 if target not matched
            if (skill[i] + skill[n-1-i] != target) return -1;

            // update chemistry on each turn.
            ans += skill[i] * skill[n-1-i];
        }

        return ans;
    }
};
