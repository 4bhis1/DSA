const max = Math.max

var maxAreaOfIsland = function (grid) {

    const ROW = grid.length
    const COL = grid[0].length

    let maxArea = 0

    const dfs = (r, c) => {
        if (
            r >= ROW ||
            r < 0 ||
            c >= COL ||
            c < 0 ||
            grid[r][c] === 0 ||
            grid[r][c] === 2
        ) {
            return 0
        }

        grid[r][c] = 2

        return dfs(r + 1, c) +
            dfs(r - 1, c) +
            dfs(r, c + 1) +
            dfs(r, c - 1) +
            1
    }


    for (let r = 0; r < ROW; r++) {
        for (let c = 0; c < COL; c++) {
            if (grid[r][c] === 1) {
                maxArea = max(maxArea, dfs(r, c))
            }
        }
    }

    return maxArea
};