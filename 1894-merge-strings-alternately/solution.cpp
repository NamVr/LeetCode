class Solution {
public:
    string mergeAlternately(string word1, string word2) {
        string str = "";
        int len1 = word1.length();
        int len2 = word2.length();
        
        int m = max(len1,len2);

        for (int i = 0; i < m; i++) {
            if (i < len1)
                str += word1[i];

            if (i < len2)
                str += word2[i];
        }

        return str;
    }
};
