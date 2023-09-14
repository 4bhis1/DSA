var exist = function (board, word) {

    const ROW = board.length
    const COL = board[0].length

    // using set so that our dfs don't get struck in circular loop
    const set = new Set()

    const dfs = (r, c, i) => {

        if (i === word.length) {
            return true
        }

        if (
            r >= ROW ||
            c >= COL ||
            r < 0 ||
            c < 0 ||
            board[r][c] != word[i] ||
            set.has(`${r}-${c}`)
        ) {
            return false
        }

        set.add(`${r}-${c}`)

        const res = dfs(r + 1, c, i + 1) ||
            dfs(r - 1, c, i + 1) ||
            dfs(r, c + 1, i + 1) ||
            dfs(r, c - 1, i + 1)

        set.delete(`${r}-${c}`)

        return res
    }

    for (let r = 0; r < ROW; r++) {
        for (let c = 0; c < COL; c++) {
            if (dfs(r, c, 0)) {
                return true
            }
        }
    }

    return false
};
