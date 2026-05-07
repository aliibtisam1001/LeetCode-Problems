class Solution(object):
    def thirdMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n=set(nums)
        num=list(n)
        if (len(num) == 1):
            return num[0]
        if(len(num) == 2):
            return (max(num))
        num.remove(max(num))
        num.remove(max(num))
        return max(num)
        