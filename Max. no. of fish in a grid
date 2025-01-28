/**
 * @param {number[][]} grid
 * @return {number}
 */
var findMaxFish = function (grid) {
    const rows = grid.length;
    const cols = grid[0].length;
    let maxFish = 0;

    // Directions for adjacent cells: right, left, down, up
    const directions = [
        [0, 1], [0, -1], [1, 0], [-1, 0]
    ];

    // Helper function for DFS
    function dfs(r, c) {
        // Base case: if the cell is out of bounds or is land
        if (r < 0 || c < 0 || r >= rows || c >= cols || grid[r][c] === 0) {
            return 0;
        }

        // Collect the fish at the current cell
        let fish = grid[r][c];
        grid[r][c] = 0; // Mark the cell as visited

        // Explore all adjacent cells
        for (const [dr, dc] of directions) {
            fish += dfs(r + dr, c + dc);
        }

        return fish;
    }

    // Iterate over every cell in the grid
    for (let r = 0; r < rows; r++) {
        for (let c = 0; c < cols; c++) {
            if (grid[r][c] > 0) { // Start DFS from every water cell
                maxFish = Math.max(maxFish, dfs(r, c));
            }
        }
    }

    return maxFish;
};
