# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        l = 0
        r = n

        while l <= r:
            mid = (l + r) // 2
            is_bad = isBadVersion(mid)

            if is_bad:
                r = mid - 1 
            else:
                l = mid + 1

        return l