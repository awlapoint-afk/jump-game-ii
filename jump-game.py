class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        if n == 1:
            return 0

        jumps = 0

        i = 0
        while i < n:
            # if current position gets us to the end
            if i + nums[i] >= n - 1:
                return jumps + 1

            bucket = []
            for j in range(i + 1, i + nums[i] + 1):
                if j >= n:
                    break
                bucket.append((j + nums[j], j))

            best = max(bucket)
            if best[1] >= n - 1:
                return jumps + 1
            i = best[1]
            jumps += 1

        return jumps


solution = Solution()

test1 = [2,3,1,1,4]
test2 = [2,3,0,1,4]
test3 = [0]

result1 = 2
result2 = 2
result3 = 0

tests = [[test1, result1], [test2, result2], [test3, result3]]

for test in tests:
    result = solution.jump(test[0])
    if result != test[1]:
        print(f"failed {test} result {result}")
    else:
        print(f"passed {test} result {result}")

print(solution.jump([1]) == 0)
print(solution.jump([2,1]) == 1)
print(solution.jump([2,3,1]) == 1)
#print(solution.jump([1,1,1,1]))
#print(solution.jump([2,3,1,1,4]))
#print(solution.jump([1,2,3]) == 2)
print(solution.jump([1,2,1,1,1]))
