class Solution:
    def generateParenthesis(self, n: int) -> List[str]:

        sequences = []

        self.backtrack(sequences, "(", 1, 0, n)

        return sequences
        

    def backtrack(self, sequences, currseq, starting, closing, n):

        print(f"Before calling func: {currseq} {starting} {closing}")


        if starting == n and closing == n:
            print("appending: " + currseq)
            sequences.append(currseq)
            return
        
        if starting  <  n:
            
            
            self.backtrack(sequences, currseq + "(", starting + 1, closing, n)

        if closing < n and closing < starting:
            
           
            self.backtrack(sequences, currseq + ")", starting, closing + 1, n)
            
        
        
           

        