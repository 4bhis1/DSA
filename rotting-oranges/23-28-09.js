var orangesRotting = function (grid) {
    const COL = grid.length
    const ROW = grid[0].length

    let fresh_oranges = 0
    let time = 0

    let queue = []

    for (let i = 0; i < COL; i++) {
        for (let j = 0; j < ROW; j++) {
            if (grid[i][j] === 1) {
                fresh_oranges++
            } else if (grid[i][j] === 2) {
                queue.push([i, j])
            }

        }
    }

    const DIRECTION_ARRAY = [[1, 0], [0, 1], [-1, 0], [0, -1]]

    // dfs
    while (fresh_oranges &amp;&amp; queue.length) {
        const newQueue = []
        for (let [col, row] of queue) {
            for (let [dcol, drow] of DIRECTION_ARRAY) {
                if (
                    col + dcol > -1 &amp;&amp;
                    col + dcol < COL &amp;&amp;
                    row + drow > -1 &amp;&amp;
                    row + drow < ROW &amp;&amp;
                    grid[col + dcol][row + drow] === 1
                ) {
                    console.log(">>>> ", col, row,
                        col + dcol,
                        row + drow
                    )
                    grid[col + dcol][row + drow] = 2
                    newQueue.push([col + dcol, row + drow])
                    fresh_oranges--
                }
            }
            queue = [...newQueue]
        }
        time++
    }

    return !fresh_oranges ? time : -1

};