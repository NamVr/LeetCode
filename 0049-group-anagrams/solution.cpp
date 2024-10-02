class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        if (!strs.size()) return {{}};

        vector<vector<string>> res;

        // Now create a hashmap to store all elements.
        unordered_map<string, vector<string>> mp;

        // Sort all string elements of input array.
        // Then check if exists in hashmap.
        for (auto& i : strs) {
            string key = i;
            sort(key.begin(), key.end());

            // store all key pair values in hashmap according to sorted key
            mp[key].push_back(i);
        }

        // prepare result
        for (auto& i: mp) {
            res.push_back(i.second);
        }
        return res;
    }
};


