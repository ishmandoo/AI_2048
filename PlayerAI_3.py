from BaseAI_3 import BaseAI
import time
import math

class PlayerAI(BaseAI):
    def getMove(self, grid):
        moves = grid.getAvailableMoves()
        cells = grid.getAvailableCells()

        scores = []
        startTime = time.time()
        for depth in range(1,10):
            scores = self.getMoveScores(grid, depth, -1000000, 1000000)
            elapsedTime = time.time() - startTime
            if elapsedTime > .1:
                print(depth)
                break

        print(moves)
        print(scores)

        maxScore = -1
        bestMove = None
        for i in range(len(scores)):
            if scores[i] > maxScore:
                maxScore = scores[i]
                bestMove = moves[i]
        return bestMove

    def getMoveScores(self, grid, depth, a, b):
        moves = grid.getAvailableMoves()
        scores=[]
        for move in moves:
            newGrid=grid.clone()
            newGrid.move(move)
            score = self.Minimize(newGrid, depth - 1, a, b)
            if score > a:
                a = score
            scores.append(score)
            if b < a:
                return scores
        return(scores)

    def Minimize(self, grid, depth, a, b):
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

                    #newGrid=grid.clone()
                    grid.insertTile(cell,val)
                    score = self.Maximize(grid, depth - 1, a, b)
                    grid.setCellValue(cell, 0)
                    if score < b:
                        b = score
                    scores.append(score)
                    if b < a:
                        return min(scores)
            return(min(scores))

    def Maximize(self, grid, depth, a, b):
        if depth == 0:
            return self.heuristic(grid)

        moves = grid.getAvailableMoves()
        if len(moves) <= 0:
            return 0
            return grid.getMaxTile()
        else:
            scores = self.getMoveScores(grid, depth, a, b)
            return(max(scores))

    def getGridVals(self,grid):
        valSet=set({})
        for i in range(4):
            for j in range(4):
                if not grid.canInsert((i,j)):
                    valSet.add(grid.getCellValue((i,j)))
        return(len(valSet))

    def heuristic(self, grid):
        return len(grid.getAvailableCells()) + self.getGridVals(grid)#+ 2 * math.log(grid.map[0][0]+1, 2) + math.log(grid.map[0][1]+1, 2) + math.log(grid.map[1][0]+1, 2)
    #+ grid.canInsert((1,1)) + grid.canInsert((1,2)) + grid.canInsert((2,1)) + grid.canInsert((2, 2))
