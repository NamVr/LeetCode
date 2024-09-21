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

#include <algorithm>
using namespace std;


class Solution {
public:
    ListNode* insertGreatestCommonDivisors(ListNode* head) {
        ListNode* tmp = head;
        while (head->next != NULL) {
            int val1 = head->val;
            int val2 = head->next->val;
            int val = gcd(val1, val2);

            ListNode* node = new ListNode(val);
            node->next = head->next;
            head->next = node;

            head = head->next->next;
        }

        return tmp;
    }
};
