class Solution(object):
  def smallestPalindrome(self, s):
    """
    :type s: str
    :rtype: str
    """
    n = len(s)
    half_len = n // 2
    left_half = "".join(sorted(s[:half_len]))

    if n % 2 == 1:
      mid = s[half_len]
      return left_half + mid + left_half[::-1]
    else:
      return left_half + left_half[::-1]