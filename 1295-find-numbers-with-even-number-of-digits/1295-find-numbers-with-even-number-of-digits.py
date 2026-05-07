class Solution(object):
    def findNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count=0
        e=0
        for i in nums:
            e=0
            if(i == 0):
                e+=1
            while(i != 0):
                i=i//10
                e+=1
            if(e % 2 == 0):
                count+=1
        return count
                
        