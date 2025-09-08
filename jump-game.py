class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        if n == 1:
            return 0

        i = jumps = index_range = max_value = 0

        while i < n:
            max_value = max(i + nums[i], max_value)
            if max_value >= n - 1:
                return jumps + 1
            if i >= index_range:
                jumps += 1
                index_range = max_value
            i += 1

        return jumps

solution = Solution()

test1 = [2,3,1,1,4]
test2 = [2,3,0,1,4]
test3 = [0]
test4 = [2,1]
test5 = [2,3,1]
test6 = [1,2,1,1,1]
test7 = [1,2,3]

result1 = 2
result2 = 2
result3 = 0
result4 = 1
result5 = 1
result6 = 3
result7 = 2

tests = [[test1, result1],
         [test2, result2],
         [test3, result3],
         [test4, result4],
         [test5, result5],
         [test6, result6],
         [test7, result7]]

for test in tests:
    result = solution.jump(test[0])
    if result != test[1]:
        print(f"failed {test} result {result}")
    else:
        print(f"passed {test} result {result}")