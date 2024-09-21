class Solution {
public:
    vector<string> uncommonFromSentences(string s1, string s2) {
        unordered_map<string,int> wordCount;
        vector<string> result;

        string word;
        stringstream ss1(s1);
        while (ss1 >> word) {
            wordCount[word]++;
        }

        stringstream ss2(s2);
        while (ss2 >> word) {
            wordCount[word]++;
        }

        for (auto& it : wordCount) {
            if (it.second == 1) {
                result.push_back(it.first);
            }
        }

        return result;
    }
};
