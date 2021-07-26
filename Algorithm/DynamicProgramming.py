# -*- coding: utf-8 -*-
# @Time : 2021/7/26 22:03
# @Author : Cao yu
# @File : DynamicProgramming.py
# @Software: PyCharm


# 股票问题

class Stock(object):
    def Stock1(self, prices: list) -> int:
        detail = "给定一个数组 prices ，它的第 i 个元素 prices[i] 表示一支给定股票第 i 天的价格。" \
                 "你只能选择某一天买入这只股票，并选择在未来的某一个不同的日子 卖出该股票。" \
                 "设计一个算法来计算你所能获取的最大利润。返回你可以从这笔交易中获取的最大利润。" \
                 "如果你不能获取任何利润，返回 0 。"
        dp = [0] * len(prices)
        min_price = prices[0]
        for i in range(1, len(prices)):
            dp[i] = max(dp[i - 1], prices[i] - min_price)
            min_price = min(min_price, prices[i])
        return dp[-1]
        #优化可以用一个变量来维护dp。

    def Stock2(self, prices: list) -> int:
        detail = "给定一个数组 prices ，其中 prices[i] 是一支给定股票第 i 天的价格" \
                 "设计一个算法来计算你所能获取的最大利润。你可以尽可能地完成更多的交" \
                 "易（多次买卖一支股票）。注意：你不能同时参与多笔交易" \
                 "（你必须在再次购买前出售掉之前的股票）。"
        dp = [[0] * 2 for i in range(len(prices))]
        dp[0][1] = -prices[0]

        for j in range(1, len(prices)):
            dp[j][0] = max(dp[j - 1][0], dp[j - 1][1] + prices[j])
            dp[j][1] = max(dp[j - 1][1], dp[j - 1][0] - prices[j])

        return dp[-1][0]
        #优化可用两个变量来维护dp，或者使用贪心算法。

    def Stock3(self, prices: list) -> int:
        detail = "给定一个数组，它的第 i 个元素是一支给定的股票在第 i 天的价格。" \
                 "设计一个算法来计算你所能获取的最大利润。你最多可以完成 两笔 交易。" \
                 "注意：你不能同时参与多笔交易（你必须在再次购买前出售掉之前的股票）。"
        n = len(prices)
        buy1 = -prices[0]
        buy2 = -prices[0]
        sell1 = 0
        sell2 = 0
        for i in range(1, n):
            buy1 = max(buy1, -prices[i])
            sell1 = max(sell1, buy1 + prices[i])
            buy2 = max(buy2, sell1 - prices[i])
            sell2 = max(sell2, buy2 + prices[i])
        return sell2



