class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        result = "".join(map(str, digits))
        result_int = int(result)+1
        result_s = str(result_int)
        fi = []

        for i in range(len(result_s)):
            fi.append(int(result_s[i]))
        return fi
                

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/leethub-v4/bcilpkkbokcopmabingnndookdogmbna