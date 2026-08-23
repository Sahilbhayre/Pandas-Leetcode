class Solution(object):

  def sumGame(self, num):
    """:type num: str

    :rtype: bool
    """
    n = len(num)
    half = n // 2

    sum_left = sum(int(c) for c in num[:half] if c != "?")
    sum_right = sum(int(c) for c in num[half:] if c != "?")

    q_left = num[:half].count("?")
    q_right = num[half:].count("?")

    sum_diff = sum_left - sum_right
    q_diff = q_left - q_right

    return sum_diff * 2 != -9 * q_diff