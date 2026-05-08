class Solution(object):
    def runningSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n=[]
        sum=0
        for i in nums:
            sum+=i
            n.append(sum)
        return n
        