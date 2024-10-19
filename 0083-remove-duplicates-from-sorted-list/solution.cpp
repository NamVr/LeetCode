/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
class Solution {
public:
    ListNode* deleteDuplicates(ListNode* head) {
        if (head == nullptr || head->next == nullptr) return head;

        ListNode* curr = head->next;
        ListNode* temp = head;

        while (curr != nullptr) {
            if (curr->val == temp->val) {
                // duplicate found, remove node.
                temp->next = curr->next;
                curr = curr->next;
                continue;
            }

            // condition, save temp and iterate
            temp = curr;
            curr = curr->next;
        }

        return head;
    }
};
