/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
int getDecimalValue(struct ListNode* head) {
    int final = 0;

    while (head) {
        final = (final << 1) + head->val;

        head = head -> next;
    }

    return final;
}
