class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l, r = 0, 1 #left = price on day 1 & right = price on day 2 initially
        Pmax = 0

        while r < len(prices):
            if prices[r] > prices[l]: #profitable
                profit = prices[r] - prices[l]
                Pmax = max(Pmax, profit)
            else:
                l = r #right val lower than left then update left to right
            r +=1 #r must go on regardless
        return Pmax

        