class Solution(object):
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        lsum=0
        rsum=0
        totalsum=sum(nums)
        previousval=0
        for i in range(len(nums)):
            lsum+=previousval
            rsum=totalsum-lsum-nums[i]
            previousval=nums[i]
            if(i == 0):
                lsum=0
            if(lsum == rsum):
                return i
        return -1
        

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/leethub-v4/bcilpkkbokcopmabingnndookdogmbna