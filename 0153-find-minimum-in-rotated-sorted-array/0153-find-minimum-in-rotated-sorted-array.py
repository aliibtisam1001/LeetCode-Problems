class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l=len(nums)-1
        mid=l//2
        r=l
        le=0
        if(l == 0):
            return nums[0]
        elif(l == 1):
            if(nums[0] > nums[1]):
                return nums[1]
            else:
                return nums[0]
        while(nums[mid] != nums[r]):
            if(nums[mid] > nums[r]):
                mid=mid+1
            elif(nums[mid] < nums[r]):
                r=r-1
                mid=mid-1
        return nums[mid]

        

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/leethub-v4/bcilpkkbokcopmabingnndookdogmbna