class Solution {
    public List<Integer> eventualSafeNodes(int[][] graph) {
        List<Integer> res = new ArrayList<>();
        // edge case, if graph is null, return null result
        if (graph == null || graph.length == 0) return res;

        int n = graph.length;

        /** Value of Color:
         * 0: Not visited
         * 1: Safe
         * 2: Unsafe
         */
        
        int[] color = new int[n];

        // RUN DFS for all elements of the graph 0->n-1.
        for (int i = 0; i < n; i++) {
            if (dfs(graph, i, color)) res.add(i);
        }

        return res;
    }

    public boolean dfs(int[][] graph, int start, int[] color) {
        // If this is visited, return safe or unsafe
        if (color[start] != 0) return color[start] == 1;

        color[start] = 2; // Unsafe initially
        // Iterate all adjacent nodes from the starting node
        for (int node: graph[start]) {
            // self run recursion: if dfs is false for adjacent nodes, return false
            if (!dfs(graph, node, color)) return false;
        }

        // otherwise, set it as safe node
        color[start] = 1;

        return true; // success run of dfs

    }
}
