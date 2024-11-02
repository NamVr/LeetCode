class Solution {
public:
    bool isCircularSentence(string sentence) {
        int i = 0;
        for (; i < sentence.length()-1; i++) {
            if (sentence[i] == ' ' && sentence[i-1] != sentence[i+1]) return false;
        }

        return sentence[0] == sentence[i];
    }
};
