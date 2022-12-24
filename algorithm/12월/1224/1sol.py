# leetcode 790. Domino and Tromino Tiling

class Solution:
    def numTilings(self, n: int) -> int:
        a = [0]*(n+1)
        b = [1,1] + [0]*(n-1)
        mod = int(1e9+7)
        for i in range(2,n+1) :
            a[i] = (a[i-1] + b[i-2]) % mod
            b[i] = (b[i-1] + b[i-2] +2*a[i-1]) % mod
        return b[n]
        