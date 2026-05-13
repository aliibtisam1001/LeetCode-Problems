class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        p=[]
        l=0
        r=len(height)-1
        if(len(height) == 2):
            return min(height)
        while l < r:
            if(height[l] < height[r]):
                p.append(height[l] *(r - l))
                l+=1
            else:
                p.append(height[r] * (r-l))
                r-=1
        m=max(p)
        return m

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/leethub-v4/bcilpkkbokcopmabingnndookdogmbna