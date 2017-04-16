class ZAlgorithm(object):

    def longestSubstring(self, s):
        """
        :type s: str
        :rtype: str
        """
        z = [0 for _ in range(len(s))]
        L, R = 0, 1
        for i in range(1, len(s)):
            if R <= i or z[i - L] >= R - i:
                z[i] = (z[i - L] if i + z[i - L] < R else R - i) if R > i else 0
                while i + z[i] < len(s) and s[i + z[i]] == s[z[i]]:
                    z[i] += 1
                if i + z[i] > R:
                    L, R = i, i + z[i]
            else:
                z[i] = z[i - L]
        return z

    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        sep = '.' + '.'.join(list(s)) + '.'
        z = []
        z.append(1)
        L, R = 0, 0
        for i in range(1, len(sep)):
            z.append(0)
            z[i] = min(z[L * 2 - i], R - i) if R > i else 1
            while i - z[i] >= 0 and i + z[i] < len(sep) and sep[i - z[i]] == sep[i + z[i]]:
                z[i] += 1
            if i + z[i] > R:
                L, R = i, i + z[i]

        mlen = max(z)
        for idx in range(1, len(sep)):
            if z[idx] == mlen:
                if idx & 1:
                    center = idx // 2
                    mlen = (mlen - 1) // 2
                    return s[center - mlen: center + mlen + 1]
                else:
                    center = idx // 2
                    mlen = (mlen - 1) // 2
                    return s[center - mlen: center + mlen]

zfunc = ZAlgorithm()
print(zfunc.longestSubstring('abaabaab'))
