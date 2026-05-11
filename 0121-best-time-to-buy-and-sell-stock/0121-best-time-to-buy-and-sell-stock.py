class Solution(object):
    def maxProfit(self, prices):
        buy=[]
        j=0
        
        for i in range(len(prices)-1):
            if prices[i+1]<prices[j]:
                j=i+1

            else:
                buy.append(prices[i+1]-prices[j])
            
        if buy:
            b=max(buy)
        else:
            b=0

        return b

        
        

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/leethub-v4/bcilpkkbokcopmabingnndookdogmbna