class Solution(object):
    def exist(self, board, word):
        self.res = False
        self.m, self.n = len(board), len(board[0])

        def dfs(i, j, idx):
            if idx == len(word):
                self.res = True
                return

            if (i < 0 or i >= self.m or
                j < 0 or j >= self.n or
                board[i][j] != word[idx]):
                return

            temp = board[i][j]
            board[i][j] = '#'

            dfs(i + 1, j, idx + 1)
            dfs(i - 1, j, idx + 1)
            dfs(i, j + 1, idx + 1)
            dfs(i, j - 1, idx + 1)

            board[i][j] = temp

        for i in range(self.m):
            for j in range(self.n):
                if board[i][j] == word[0]:
                    dfs(i, j, 0)

        return self.res
        
