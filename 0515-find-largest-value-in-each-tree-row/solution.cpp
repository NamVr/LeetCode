/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
class Solution {
public:
    vector<int> largestValues(TreeNode* root) {
        if (root == nullptr) return vector<int>{};

        vector<int> res;
        queue<TreeNode*> q;
        q.push(root);

        while (!q.empty()) {
            // for each level
            int maxElement = INT_MIN;
            int n = q.size();

            for (int i = 0; i < n; i++) {
                TreeNode* node = q.front(); q.pop();

                maxElement = max(maxElement, node->val);

                if (node->left) q.push(node->left);
                if (node->right) q.push(node->right);
            }

            // once level iteration is over, return max
            res.push_back(maxElement);
        }

        return res;
    }
};
