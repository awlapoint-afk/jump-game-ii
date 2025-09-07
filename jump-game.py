class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        dp = [0] * n

        for i in range(1, n):
            jumps = []
            for j in range(0, i):
                if j + nums[j] >= i:
                    jumps.append(dp[j] + 1)
            dp[i] = min(jumps)

        return dp[-1]


solution = Solution()

test1 = [2,3,1,1,4]
test2 = [2,3,0,1,4]

result1 = 2
result2 = 2

tests = [[test1, result1], [test2, result2]]

for test in tests:
    result = solution.jump(test[0])
    if result != test[1]:
        print(f"failed {test} result {result}")
    else:
        print(f"passed {test} result {result}")