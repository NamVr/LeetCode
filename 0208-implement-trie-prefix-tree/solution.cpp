class TrieNode {
public:
    unordered_map<char,TrieNode*> children;
    bool endOfWord;

    TrieNode() {
        endOfWord = false;
    }
};

class Trie {
private:
    TrieNode* root;
public:
    Trie() {
        root = new TrieNode();
    }
    
    void insert(string word) {
        TrieNode* node = root;

        for (char ch : word) {
            if (node->children.find(ch) == node->children.end()) {
                // character is not present
                node->children[ch] = new TrieNode();
            }

            // next node
            node = node->children[ch];
        }

        // after all iteration, mark end of work
        node->endOfWord = true;
    }
    
    bool search(string word) {
        TrieNode* node = root;
        for (char ch : word) {
            if (node->children.find(ch) == node->children.end()) {
                return false;
            }

            // move to next node till possible
            node = node->children[ch];
        }

        // when all letters are traversed, check if it's end of word.
        return node->endOfWord;
    }
    
    bool startsWith(string prefix) {
        TrieNode* node = root;

        for (char ch : prefix) {
            if (node->children.find(ch) == node->children.end()) {
                return false;
            }

            node = node->children[ch];
        }

        // if iteration is successful, return true
        return true;
    }
};

/**
 * Your Trie object will be instantiated and called as such:
 * Trie* obj = new Trie();
 * obj->insert(word);
 * bool param_2 = obj->search(word);
 * bool param_3 = obj->startsWith(prefix);
 */
