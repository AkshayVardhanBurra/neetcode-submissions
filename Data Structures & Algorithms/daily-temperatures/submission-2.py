class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:


        monotonic_dec = []
        result = [0] * len(temperatures)


        for i in range(len(temperatures) - 1, -1, -1):
            
            if len(monotonic_dec) == 0:
                monotonic_dec.append(i)
                result[i] = 0

            while(len(monotonic_dec) > 0 and temperatures[monotonic_dec[len(monotonic_dec) - 1]] <= temperatures[i]):
                monotonic_dec.pop()
            

            if(len(monotonic_dec) == 0):
                result[i] = 0
                monotonic_dec.append(i)

            else:
                result[i] = monotonic_dec[len(monotonic_dec) - 1] - i
                monotonic_dec.append(i)

        return result

        



    

    
        

    



        