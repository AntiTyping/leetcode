func isValidSudoku(board [][]byte) bool {
    var rows, cols, boxes [9][9]bool

    for r := 0; r < 9; r++ {
        for c := 0; c < 9; c++ {
            ch := board[r][c]

            if ch == '.' {
                continue
            }

            v := ch - '1'

            if rows[r][v] == true {
                return false
            }
            if cols[c][v] == true {
                return false
            }

            b := 3 * (r / 3) + c / 3

            if boxes[b][v] == true {
                return false
            }

            rows[r][v] = true
            cols[c][v] = true
            boxes[b][v] = true
        }
    }

    return true
}