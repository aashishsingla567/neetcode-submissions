
BOARD_X_MAX = 9
BOARD_Y_MAX = 9
BOX_X_MAX = 3
BOX_Y_MAX = 3

class Solution:

    def check_box(self, x: int, y: int) -> bool:
        board = self.board
        
        s = set()
        for i in range(x, x + BOX_X_MAX):
            for j in range(y, y + BOX_Y_MAX):
                num = board[i][j]
                if num == '.':
                    continue
                if num in s:
                    return False
                s.add(num)
        return True

    def check_row(self, x: int, y: int) -> bool:
        board = self.board

        s = set()

        for j in range(BOARD_Y_MAX):
            num = board[x][j]
            if num == '.':
                continue
            if num in s:
                return False
            s.add(num)
        return True

    def check_column(self, x: int, y: int) -> bool:
        board = self.board

        s = set()
        for i in range(BOARD_X_MAX):
            num = board[i][y]
            if num == '.':
                continue
            if num in s:
                return False
            s.add(num)
        return True

    def isValidSudoku(self, board: List[List[str]]) -> bool:
        self.board = board

        for i in range(len(board)):
            if not self.check_row(i, 0):
                return False
    
        for j in range(len(board)):
            if not self.check_column(0, j):
                return False
    
        for i in range(0, len(board), 3):
            for j in range(0, len(board), 3):
                if not self.check_box(i, j):
                    return False

        return True
