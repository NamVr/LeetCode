/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */

class Solution {
    private Deque<Integer> preorderDeque;
    private HashMap<Integer, Integer> inorderMap;

    public TreeNode buildTree(int[] preorder, int[] inorder) {
        // init the preorder deque
        preorderDeque = new LinkedList<>();
        for (int val : preorder) {
            preorderDeque.addLast(val);
        }

        // hashmap for val : i wrt to inorder array
        inorderMap = new HashMap<>();
        for (int i = 0; i < inorder.length; i++) {
            inorderMap.put(inorder[i], i);
        }

        // recursion returns root node
        return helper(0, inorder.length - 1);
    }

    private TreeNode helper(int l, int r) {
        // Base case: impossible
        if (l > r) {
            return null;
        }

        // first element is always the root in preorder
        int rootVal = preorderDeque.removeFirst();
        TreeNode root = new TreeNode(rootVal);

        // get m from inorder array.
        int m = inorderMap.get(rootVal);

        // recursion
        root.left = helper(l, m - 1);
        root.right = helper(m + 1, r);

        return root;
    }
}
