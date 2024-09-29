class Node {
public:
    Node* prev;
    Node* next;
    int count;
    unordered_set<string> keys;

    Node() : prev(nullptr), next(nullptr), count(0) {}

    Node(const string& key, int count) : prev(nullptr), next(nullptr), count(count) {
        keys.insert(key);
    }

    // Insert node after this node.
    Node* insert(Node* node) {
        node->prev = this;
        node->next = this->next;
        this->next->prev = node;
        this->next = node;
        return node;
    }

    void remove() {
        this->prev->next = this->next;
        this->next->prev = this->prev;
    }
};

class AllOne {
private:
    Node root;
    unordered_map<string, Node*> nodes;

public:
    AllOne() {
        root.next = &root;
        root.prev = &root;
    }
    
    void inc(string key) {
        if (nodes.find(key) == nodes.end()) {
            // key not found
            if (root.next == &root || root.next->count > 1) {
                nodes[key] = root.insert(new Node(key, 1));
            } else {
                root.next->keys.insert(key);
                nodes[key] = root.next;
            }
        } else {
            // key is found, move to next node
            Node* current = nodes[key];
            Node* next = current->next;

            if (next == &root || next->count > current->count + 1) {
                nodes[key] = current->insert(new Node(key, current->count+1));  
            } else {
                next->keys.insert(key);
                nodes[key] = next;
            }

            // remove key from current node & delete it node is empty
            current->keys.erase(key);
            if (current->keys.empty()) {
                current->remove();
                delete current;
            }
        }
    }
    
    void dec(string key) {
        auto it = nodes.find(key);
        if (it == nodes.end()) return; // not needed
        Node *current = it->second;

        if (current->count == 1) {
            // remove the key completely
            nodes.erase(key);
        } else {
            // Move the key to prev node / create new node
            Node *prev = current->prev;
            if (prev == &root || prev->count < current->count - 1) {
                nodes[key] = prev->insert(new Node(key, current->count - 1));
            } else {
                prev->keys.insert(key);
                nodes[key] = prev;
            }
        }

        // remove key from current node
        current->keys.erase(key);
        if (current->keys.empty()) {
            current->remove();
            delete current;
        }
    }
    
    string getMaxKey() {
        if (root.prev == &root) return ""; // no keys
        return *root.prev->keys.begin();
    }
    
    string getMinKey() {
        if (root.prev == &root) return ""; // no keys
        return *root.next->keys.begin();
    }
};

/**
 * Your AllOne object will be instantiated and called as such:
 * AllOne* obj = new AllOne();
 * obj->inc(key);
 * obj->dec(key);
 * string param_3 = obj->getMaxKey();
 * string param_4 = obj->getMinKey();
 */
