class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        level = 0;
        rowSet = set()
        boardMap = {
            0:set(),
            1:set(),
            2:set(),
            3:set(),
            4:set(),
            5:set(),
            6:set(),
            7:set(),
            8:set()
        }

        #checking rows an boxes
        print(len(board))
        for i in range(0, len(board)):

            row = board[i]
            print(i)
            if(i % 3 == 0 and i != 0):
                level += 1

            for j in range(0, len(row)):
                if(row[j] != '.'):
                    if row[j] in rowSet:
                        print("False because there is a repeat in a row")
                        return False
                        
                    else:
                        rowSet.add(row[j])
                    
                    if self.checkAndAdd(boardMap, int(j/3) + (level * 3), row[j]) == False:
                        print("False because it has a repeat in a box.")
                        return False
            
            rowSet = set()


        return self.checkColumns(board)
        

    def checkColumns(self, board):
        colSet = set()
        boardRows = len(board[0])
        for i in range(0, boardRows):
            for j in range(0, len(board)):
                if(board[j][i] != "."):
                    if board[j][i] in colSet:
                        print("the repeat is : " + str(board[j][i]))
                        print("false because there is a duplicate in the column")
                        return False
                        
                    else:
                        colSet.add(board[j][i])
            colSet = set()
        return True
    
    def checkAndAdd(self, sectionMap, section, val):
    
        sectionSet = sectionMap[section];
 
        if val in sectionSet:
            print("returning false in the method!")
            return False
        else:
            sectionSet.add(val)
            return True
        