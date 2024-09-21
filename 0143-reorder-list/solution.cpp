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
    void reorderList(ListNode* head) {
        // Dividing LinkedList into 2 parts

        ListNode* slow = head;
        ListNode* fast = head->next;
        while (fast != nullptr && fast->next != nullptr) {
            slow = slow->next;
            fast = fast->next->next;
        }

        // Reversing LinkedList (2nd half)

        ListNode* second = slow->next;
        ListNode* prev = nullptr;
        slow->next = nullptr; // defining the end of the linkedlist

        while (second != nullptr) {
            ListNode* next = second->next;
            second->next = prev;
            prev = second;
            second = next;
        }

        // Applying the algorithm:
        
        ListNode* first = head;
        second = prev;
        
        while (second != nullptr) {
            ListNode* tmp1 = first->next;
            ListNode* tmp2 = second->next;
        
            first->next = second;
            second->next = tmp1;
        
            first = tmp1;
            second = tmp2;
        }
    }
};
