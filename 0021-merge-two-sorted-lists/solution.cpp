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
    ListNode* mergeTwoLists(ListNode* list1, ListNode* list2) {
        ListNode* tmp1 = list1;
        ListNode* tmp2 = list2;
        ListNode* head = new ListNode();
        ListNode* final = head;

        while (tmp1 != nullptr && tmp2 != nullptr) {
            if (tmp1->val <= tmp2->val) {
                final->next = tmp1;
                tmp1 = tmp1->next;
            } else {
                final->next = tmp2;
                tmp2 = tmp2->next;
            }
            final = final->next;
        }

        if (tmp1 != nullptr) {
            final->next = tmp1;
        } else if (tmp2 != nullptr) {
            final->next = tmp2;
        }

        return head->next;
    }
};
