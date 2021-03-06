class Solution:
    def maxProfit(self, prices):
        # write code here
        if "S" in prices[0]:
            minn = int(prices[0][0]) * 7
        else:
            minn = int(prices[0][0])
        ans = 0
        for i in range(len(prices)):
            print(prices[i], type(prices[i]))
            print(prices[i][0], prices[i][1])
            if "S" in prices[i]:
                value = int(prices[i][0]) * 7
            else:
                value = int(prices[i][0])
            minn = min(minn, value)
            ans = max(ans, value - minn)
        return ans
str = "2Y 3S 4S 6Y 8S"
list1 = str.split(" ")
s = Solution()
print(s.maxProfit(list1))
