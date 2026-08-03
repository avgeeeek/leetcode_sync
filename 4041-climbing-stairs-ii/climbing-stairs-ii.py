class Solution:
    def climbStairs(self, n: int, costs: List[int]) -> int:
        dp = [-1] * (n + 1)

        def solve(i: int) -> int:
            if i > n:
                return float('inf')
            if i == n:
                return 0
            if dp[i] != -1:
                return dp[i]

            oneStep = (costs[i] + 1) + solve(i + 1)
            twoStep = (costs[i + 1] + 4 + solve(i + 2)) if i + 2 <= n else float('inf')
            threeStep = (costs[i + 2] + 9 + solve(i + 3)) if i + 3 <= n else float('inf')

            dp[i] = min(oneStep, twoStep, threeStep)
            return dp[i]

        return solve(0)