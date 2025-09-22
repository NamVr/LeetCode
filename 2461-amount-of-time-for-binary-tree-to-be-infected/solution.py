# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def amountOfTime(self, root: Optional[TreeNode], start: int) -> int:
        # Step 1: Convert the binary tree into an undirected graph
        # This helper function performs a Depth First Search (DFS)
        # to build an adjacency list representation of the tree.
        def dfs(node):
            # Base case: if the node is None, stop the recursion.
            if not node:
                return

            # If the current node has a left child, add an edge between
            # the current node and its left child in both directions
            # to the graph (since disease can spread up or down).
            if node.left:
                graph[node.val].append(node.left.val)
                graph[node.left.val].append(node.val)

            # If the current node has a right child, add an edge between
            # the current node and its right child in both directions.
            if node.right:
                graph[node.val].append(node.right.val)
                graph[node.right.val].append(node.val)
                
            # Recursively call dfs on the left and right children
            # to continue building the graph.
            dfs(node.left)
            dfs(node.right)

        # Initialize an adjacency list using defaultdict for the graph.
        # graph[node_val] will store a list of neighbors for node_val.
        graph = defaultdict(list)
        
        # Call the dfs function starting from the root to populate the graph.
        dfs(root)

        # Step 2: Perform a Breadth First Search (BFS) starting from the 'start' node
        # to find the maximum time it takes for the infection to spread to all reachable nodes.
        
        # Keep track of visited nodes to avoid cycles and redundant processing.
        visited = set()
        
        # Initialize a deque (double-ended queue) for BFS, starting with the 'start' node.
        queue = deque([start])
        
        # Initialize time counter. It's set to -1 because the first level (the start node itself)
        # corresponds to 0 minutes, and the loop increments 'time' before processing the level.
        time = -1
        
        # Continue BFS as long as there are nodes in the queue.
        while queue:
            # Increment time for the current level of infection spread.
            time += 1
            
            # Get the number of nodes at the current level.
            # This is important to process all nodes at the current 'time' level
            # before moving to the next level (next increment of 'time').
            for _ in range(len(queue)):
                # Dequeue a node from the front of the queue.
                current_node = queue.popleft()
                
                # Mark the current node as visited.
                visited.add(current_node)
                
                # Iterate through all neighbors of the current node.
                for neighbor in graph[current_node]:
                    # If a neighbor has not been visited yet, it means it's a new node
                    # to be infected at the next time step.
                    if neighbor not in visited:
                        # Enqueue the unvisited neighbor.
                        queue.append(neighbor)
                        # Mark the neighbor as visited immediately to avoid adding it
                        # to the queue multiple times if it has multiple paths from `start`
                        # or if other nodes at the current BFS level also connect to it.
                        # (This is a common optimization for BFS on graphs with potentially many edges).
                        visited.add(neighbor) # Add this to prevent duplicate queueing and processing
        
        # The 'time' variable now holds the maximum distance (in minutes)
        # from the 'start' node to any other node in the graph.
        return time
