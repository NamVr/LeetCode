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
    ListNode* mergeKLists(vector<ListNode*>& lists) {
        vector<int> arr;
        for (auto l : lists) {
            while (l != nullptr) {
                arr.push_back(l->val);
                l = l->next;
            }
        }

        if (arr.empty()) {
            return nullptr;
        }

        sort(arr.begin(), arr.end());
        ListNode* head = new ListNode(arr.front());
        ListNode* curr = head;
        for (int i = 1; i < arr.size(); i++) {
            ListNode* node = new ListNode(arr[i]);
            curr->next = node;
            curr = curr->next;
        }
        return head;
    }
};
