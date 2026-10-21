class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        i = 0
        row = [set() for x in range(9)]
        col = [set() for x in range(9)]
        box = [set() for x in range(9)]
        for ROW in board:
            j = 0
            for COL in ROW:
                BOX = i - (i%3) + j//3
                term = board[i][j]
                if term == ".":
                    j += 1
                    continue
                if term in row[i] or term in col[j] or term in box[BOX]:
                    return False
                row[i].add(term)
                col[j].add(term)
                box[BOX].add(term)
                j += 1
            i += 1
        return True