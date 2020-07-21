from typing import List


class WordSearch:
    def exist(self, board: List[List[str]], word: str) -> bool:
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == word[0] and self.dfs(board, i, j, 0, word):
                    return True
        return False

    def dfs(self, board, i, j, count, word):
        if count == len(word):
            return True

        if i < 0 or i >= len(board) or j < 0 or j >= len(board[0]) or board[i][j] != word[count]:
            return False

        temp = board[i][j]
        board[i][j] = ' '
        found = self.dfs(board, i + 1, j, count + 1, word) or self.dfs(board, i - 1, j, count + 1, word) or self.dfs(
            board, i, j + 1, count + 1, word) or self.dfs(board, i, j - 1, count + 1, word)

        board[i][j] = temp
        return found


obj = WordSearch()
print(obj.exist([['A', 'B', 'C', 'E'], ['S', 'F', 'C', 'S'], ['A', 'D', 'E', 'E']]))