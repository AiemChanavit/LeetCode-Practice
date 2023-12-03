class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :type: int
        """
        # maxProf = 0
        # minPrice = 99999

        # for i in range(len(prices)):
        #     if prices[i] < minPrice:
        #         minPrice = prices[i]

        #     for j in range(i+1, len(prices)):
        #         if maxProf < (prices[j] - minPrice):
        #             maxProf = prices[j] - minPrice
        # return maxProf

        left = 0
        right = 1
        maxProf = 0

        while right < len(prices):
            if prices[right] > prices[left]:
                currentProfit = prices[right] - prices[left]
                maxProf = max(maxProf, currentProfit)
            
            else:
                left = right
            right += 1
        
        return maxProf



solution_instance = Solution()
prices = [7,6,4,3,1]
result = solution_instance.maxProfit(prices)
print(result)
