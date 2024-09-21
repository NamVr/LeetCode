#include <vector>
#include <queue>

using namespace std;

class Solution {
public:
    void bfs(int r, int c, int rows, int cols, vector<vector<char>>& grid, vector<vector<bool>>& visited) {
        queue<pair<int, int>> q; // exploratory queue
        visited[r][c] = true;
        q.push({r, c});

        vector<pair<int, int>> directions = {{0, 1}, {1, 0}, {-1, 0}, {0, -1}};
        
        while (!q.empty()) {
            int row = q.front().first;
            int col = q.front().second;
            q.pop();
            
            for (int i = 0; i < directions.size(); i++) {
                int dr = row + directions[i].first;
                int dc = col + directions[i].second;
                
                if (dr >= 0 && dr < rows && dc >= 0 && dc < cols && grid[dr][dc] == '1' && !visited[dr][dc]) {
                    q.push({dr, dc});
                    visited[dr][dc] = true;
                }
            }
        }
    }
    
    int numIslands(vector<vector<char>>& grid) {
        if (grid.empty()) return 0;
        int rows = grid.size(), cols = grid[0].size();
        int islands = 0;
        vector<vector<bool>> visited(rows, vector<bool>(cols, false));
        
        for (int r = 0; r < rows; r++) {
            for (int c = 0; c < cols; c++) {
                
                if (grid[r][c] == '1' && !visited[r][c]) {
                    bfs(r, c, rows, cols, grid, visited);
                    islands++; // found
                }
            }
        }
        
        return islands;
    }
};

