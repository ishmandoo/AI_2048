from BaseAI_3 import BaseAI

class PlayerAI(BaseAI):
    def getMove(self, grid):
        moves = grid.getAvailableMoves()
        scores = self.getMoveScores(grid, 3)

        print(moves)
        print(scores)

        maxScore = -1
        bestMove = None
        for i in range(len(moves)):
            if scores[i] > maxScore:
                maxScore = scores[i]
                bestMove = moves[i]
        return bestMove

    def getMoveScores(self, grid, depth):
        moves = grid.getAvailableMoves()
        scores=[]
        for move in moves:
            newGrid=grid.clone()
            newGrid.move(move)
            scores.append(self.Minimize(newGrid, depth - 1))
        return(scores)

    def Minimize(self, grid, depth):
        if depth == 0:
            return self.heuristic(grid)

        cells = grid.getAvailableCells()

        if len(cells) <= 0:
            return 0
            return grid.getMaxTile()
        else:
            scores=[]
            for cell in cells:
                for val in [2,4]:
                    newGrid=grid.clone()
                    newGrid.insertTile(cell,val)
                    scores.append(self.Maximize(newGrid, depth - 1))
            return(min(scores))

    def Maximize(self, grid, depth):
        if depth == 0:
            return self.heuristic(grid)

        moves = grid.getAvailableMoves()
        if len(moves) <= 0:
            return 0
            return grid.getMaxTile()
        else:
            scores = self.getMoveScores(grid, depth)
            return(max(scores))

    def heuristic(self, grid):
        return len(grid.getAvailableCells())
