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
    bool flipEquiv(TreeNode* root1, TreeNode* root2) {
        // Both roots are null, they are equivalent
        if (!root1 && !root2) return true;
        // One is null and the other isn't, they are not equivalent
        if (!root1 || !root2) return false;
        // Values are not equal, trees are not equivalent
        if (root1->val != root2->val) return false;

        // Check both cases:
        // 1. No flip: left of root1 with left of root2 and right of root1 with right of root2
        // 2. Flip: left of root1 with right of root2 and right of root1 with left of root2
        // if either of the condition is satisfied, then return true
        return (flipEquiv(root1->left, root2->left) && flipEquiv(root1->right, root2->right)) || (flipEquiv(root1->left, root2->right) && flipEquiv(root1->right, root2->left));
    }
};
