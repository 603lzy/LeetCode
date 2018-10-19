class Solution(object):
    def countlive(self, i, j, board, nrow, ncol):  #count hte live sells in 8 cells
        """
        :param i: int position
        :param j: int position
        :return: int number of live cell around
        """
        cnt = 0
        if i:
            cnt += board[i - 1][j]
            if j:
                cnt += board[i - 1][j - 1]
            if j != ncol - 1:
                cnt += board[i - 1][j + 1]
        if j:
            cnt += board[i][j - 1]
        if j != ncol - 1:
            cnt += board[i][j + 1]
        if i != nrow - 1:
            cnt += board[i + 1][j]
            if j:
                cnt += board[i + 1][j - 1]
            if j != ncol - 1:
                cnt += board[i + 1][j + 1]
        return cnt

    def gameOfLife(self, board):
        """
        :type board: List[List[int]]
        :rtype: void Do not return anything, modify board in-place instead
        """
        nrow = len(board)
        ncol = len(board[0])
        live = []
        for i in range(nrow):
            for j in range(ncol):
                cnt = self.countlive(i, j, board, nrow, ncol)
                if board[i][j]:
                    if 2 <= cnt <= 3:
                        live.append([i, j])
                if not board[i][j]:
                    if cnt == 3:
                        live.append([i, j])

        for i in range(nrow):
            for j in range(ncol):
                board[i][j] = 1 if [i, j] in live else 0

        return
