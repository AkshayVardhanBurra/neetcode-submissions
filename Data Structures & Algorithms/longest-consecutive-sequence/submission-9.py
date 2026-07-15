class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        smallest = nums[0]
        biggest = nums[0]

        for num in nums:
            if num < smallest:
                smallest = num

            if num > biggest:
                biggest = num
        
  
        bucketArray = [0] * (biggest - smallest + 1)
        
        containsZero = self.initializeBucketArray(bucketArray, smallest, nums)
        print(bucketArray)

        
            

        
        return self.countLongestSequence(bucketArray, smallest, containsZero)


    def normalizeCount(self, count):
        if count == 0:
            return 1
        return count

    def createSet(self, nums):
        newSet = set()

        for num in nums:
            newSet.add(num)

        return newSet

    def initializeBucketArray(self, bucketArray, smallest, nums):
        containsZero = False
        for num in nums:
            if num == 0:
                containsZero = True
            bucketArray[num - smallest] = num

        return containsZero
    
    def countLongestSequence(self, buckets, smallest, containsZero):
        longestCount = 0
        count = 0
        prev = 0
        firstTime = True
        zeroIndex = -1

        if containsZero:
            zeroIndex = 0 - smallest
        
        for i in range(len(buckets)):
            if i == zeroIndex or buckets[i] != 0:
                if firstTime:
                    count += 1
                    prev = buckets[i]
                    firstTime = False
                elif prev + 1 == buckets[i]:
                    count += 1
                    prev = buckets[i]
                elif prev == buckets[i]:
                    continue
                else:
                    if count > longestCount:
                        longestCount = count
                    count = 1
                    prev = buckets[i]
        
        if count > longestCount:
            return count

        else:
            return longestCount
        
        