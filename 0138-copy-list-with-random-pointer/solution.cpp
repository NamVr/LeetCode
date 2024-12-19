/*
// Definition for a Node.
class Node {
public:
    int val;
    Node* next;
    Node* random;
    
    Node(int _val) {
        val = _val;
        next = NULL;
        random = NULL;
    }
};
*/

class Solution {
public:
    Node* copyRandomList(Node* head) {
        unordered_map<Node*,Node*> m; // hashmap for references
        m[NULL] = NULL; // for edge case, null points to null

        Node* curr = head;
        while (curr != NULL) {
            Node* copy = new Node(curr->val);
            m[curr] = copy;
            curr = curr->next;
        }

        curr = head;
        while (curr != NULL) {
            Node* copy = m[curr];
            copy->next = m[curr->next];
            copy->random = m[curr->random];
            curr = curr->next;
        }

        return m[head];
    }
};
