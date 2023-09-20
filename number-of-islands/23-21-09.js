var numIslands = function (grid) {

    const ROW = grid.length
    const COL = grid[0].length

    const dfs = (r, c) => {
        if (r >= ROW ||
            c >= COL ||
            c < 0 ||
            r < 0 ||
            grid[r][c] === "0" ||
            grid[r][c] === "2"
        ) {
            return
        }

        grid[r][c] = '2'

        dfs(r + 1, c)
        dfs(r, c + 1)
        dfs(r - 1, c)
        dfs(r, c - 1)
    }

    let noOfIlands = 0

    for (let i = 0; i < ROW; i++) {
        for (let j = 0; j < COL; j++) {
            if (grid[i][j] === '1') {
                dfs(i, j)
                noOfIlands++
            }
        }
    }

    return noOfIlands

};