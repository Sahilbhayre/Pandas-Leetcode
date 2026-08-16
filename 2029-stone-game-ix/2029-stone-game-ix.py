class Solution(object):
    def stoneGameIX(self, stones):
        """
        :type stones: List[int]
        :rtype: bool
        """
        cnt = [0] * 3
        for stone in stones:
            cnt[stone % 3] += 1
        
        if cnt[0] % 2 == 0:
            return cnt[1] >= 1 and cnt[2] >= 1
        else:
            return abs(cnt[1] - cnt[2]) > 2