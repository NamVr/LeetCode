class Solution {
public:
    bool areSentencesSimilar(string sentence1, string sentence2) {
        // split sentence into words " "
        auto splitW = [](const string& sentence) {
            vector<string> words;
            string word = "";
            for (char c : sentence) {
                if (c == ' ') {
                    if (!word.empty()) {
                        words.push_back(word);
                        word = "";
                    }
                } else {
                    word += c;
                }
            }
            if (!word.empty()) words.push_back(word);
            return words;
        };

        vector<string> words1 = splitW(sentence1);
        vector<string> words2 = splitW(sentence2);

        // get longer sentence
        if (words1.size() < words2.size()) swap(words1, words2);
        int n1 = words1.size(), n2 = words2.size();

        // do comparision from start and end
        int start = 0, end = 0;
        
        while (start < n2 && words1[start] == words2[start]) start++;
        while (end < n2 && words1[n1-end-1] == words2[n2-end-1]) end++;

        // check if remaining part is in middle
        return start + end >= n2;
    }
};
