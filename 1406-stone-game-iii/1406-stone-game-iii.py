class Solution(object):
    def stoneGameIII(self, stoneValue):
        """
        :type stoneValue: List[int]
        :rtype: str
        """
        n = len(stoneValue)
        dp = [0] * 4

        for i in range(n - 1, -1, -1):
            take_one = stoneValue[i] - dp[(i + 1) % 4]
            
            take_two = float('-inf')
            if i + 1 < n:
                take_two = stoneValue[i] + stoneValue[i + 1] - dp[(i + 2) % 4]
            
            take_three = float('-inf')
            if i + 2 < n:
                take_three = stoneValue[i] + stoneValue[i + 1] + stoneValue[i + 2] - dp[(i + 3) % 4]

            dp[i % 4] = max(take_one, take_two, take_three)

        alice_score_diff = dp[0]

        if alice_score_diff > 0:
            return "Alice"
        elif alice_score_diff < 0:
            return "Bob"
        else:
            return "Tie"