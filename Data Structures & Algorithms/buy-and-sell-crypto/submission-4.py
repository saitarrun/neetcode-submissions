class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        # bruteforce 
        # res = 0
        # for i in range(len(prices)):
        #     buy = prices[i]
        #     for j in range(i+1, len(prices)):
        #         sell = prices[j]
        #         res = max(res, sell - buy)
        # return res


        l = 0
        r = 1
        res = 0

        while r < len(prices):
            # check if profitable
            if prices[l] < prices[r]:
                res = max(res,prices[r] - prices[l])
            else:
                l = r 
            r += 1
        return res

