class Solution:
    def recoverFromPreorder(self, traversal: str) -> Optional[TreeNode]:
        stack = []  # Stack to maintain nodes at each depth
        i, length = 0, len(traversal)

        while i < length:
            # Count the number of dashes indicating depth
            depth = 0
            while i < length and traversal[i] == "-":
                depth += 1
                i += 1

            # Extract the numerical value for the node
            value = 0
            while i < length and traversal[i].isdigit():
                value = value * 10 + int(traversal[i])
                i += 1

            node = TreeNode(value)

            # Update the stack to maintain the current node at the correct depth
            if depth < len(stack):
                stack[depth] = node
            else:
                stack.append(node)

            # Attach the node to its parent if it's not the root
            if depth > 0:
                parent = stack[depth - 1]
                if parent.left is None:
                    parent.left = node
                else:
                    parent.right = node

        return stack[0]  # Return the root node

