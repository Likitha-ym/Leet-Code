class Solution(object):
    def numberGame(self, nums):
        nums.sort()

        arr = []

        while nums:
            alice_move = nums.pop(0)
            bob_move = nums.pop(0)

            arr.append(bob_move)
            arr.append(alice_move)

        return arr

solution = Solution()
result_example1 = solution.numberGame([5, 4, 2, 3])
print(result_example1)  # Output: [3, 2, 5, 4]

result_example2 = solution.numberGame([2, 5])
print(result_example2)  # Output: [5, 2]
