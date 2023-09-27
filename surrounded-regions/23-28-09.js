var solve = function (board) {

    const COL = board.length
    const ROW = board[0].length

    // dfs
    const dfs = (col, row) => {
        if (row < 0 ||
            col < 0 ||
            row === ROW ||
            col === COL ||
            board[col][row] === 'X'||
            board[col][row] === 'T'
        ) {
            return
        }

        board[col][row] = 'T'
        dfs(col, row + 1)
        dfs(col, row - 1)
        dfs(col + 1, row)
        dfs(col - 1, row)
    }

    //capturing only 0 which are at the edges
    for (let col = 0; col < COL; col++) {
        for (let row = 0; row < ROW; row++) {
            if (
                board[col][row] === 'O' &amp;&amp;
                (col === 0 ||
                    row === 0 ||
                    col === COL - 1 ||
                    row === ROW - 1)
            ) {
                dfs(col, row)
            }
        }
    }

    for (let col = 0; col < COL; col++) {
        for (let row = 0; row < ROW; row++) {
            if (board[col][row] === 'O') {
                board[col][row] = 'X'
            }
        }
    }


    for (let col = 0; col < COL; col++) {
        for (let row = 0; row < ROW; row++) {
            if (board[col][row] === 'T') {
                board[col][row] = 'O'
            }
        }
    }



    return board

}; 