class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        count=0
        for j in range(len(nums)):
            if(nums[j] != 0):
                nums[count],nums[j]=nums[j],nums[count]
                count+=1
        return nums