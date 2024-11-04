class Solution {
public:
    string compressedString(string word) {
        int n = word.length();
        string comp;

        for (int i = 0, j = 0; i<n; i = j) {
            int count = 0;
            while (j < n && word[j] == word[i] && count < 9) {
                j++;
                count++;
            }
            comp += to_string(count) + word[i];
        }

        return comp;
    }
};
