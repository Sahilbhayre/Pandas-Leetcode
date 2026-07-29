from collections import Counter

class Solution(object):
    def smallestPalindrome(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        counts = Counter(s)
        
        # Identify middle character if length is odd and calculate half frequencies
        mid_char = ""
        half_counts = {}
        for ch, cnt in counts.items():
            if cnt % 2 != 0:
                mid_char = ch
            half_counts[ch] = cnt // 2

        half_len = len(s) // 2

        # Helper function to compute total permutations of current frequencies capped at limit + 1
        def num_ways(freq_list, total_len, limit):
            ans = 1
            rem = total_len
            for f in freq_list:
                if f <= 0:
                    continue
                # Use min(f, rem - f) for symmetry optimization
                r = min(f, rem - f)
                c = 1
                for j in range(1, r + 1):
                    c = c * (rem - r + j) // j
                    if c > limit:
                        c = limit + 1
                        break
                ans *= c
                if ans > limit:
                    return limit + 1
                rem -= f
            return ans

        # Check if total distinct palindromic permutations are fewer than k
        freq_list = list(half_counts.values())
        total_perms = num_ways(freq_list, half_len, k)
        if total_perms < k:
            return ""

        # Construct the left half character by character
        left_half = []
        chars = sorted(half_counts.keys())

        for i in range(half_len):
            rem_len = half_len - 1 - i
            for ch in chars:
                if half_counts[ch] > 0:
                    half_counts[ch] -= 1
                    
                    freqs = [half_counts[c] for c in chars if half_counts[c] > 0]
                    ways = num_ways(freqs, rem_len, k)
                    
                    if k <= ways:
                        left_half.append(ch)
                        break
                    else:
                        k -= ways
                        half_counts[ch] += 1

        left_str = "".join(left_half)
        return left_str + mid_char + left_str[::-1]