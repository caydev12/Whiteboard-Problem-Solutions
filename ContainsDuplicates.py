class Solution:
    def hasDuplicate(self, nums):
        nums.sort()
        for i in range(1, len(nums)):
            if nums[i] == nums[i - 1]:
                return True
        return False

if __name__ == "__main__":
    sol = Solution()

    # Test cases
    tests = [
        ([1, 2, 3, 4], False),          # no duplicates
        ([1, 2, 3, 3], True),           # one duplicate
        ([5, 5, 5, 5], True),           # all duplicates
        ([], False),                    # empty list
        ([10], False),                  # single element
        ([2, 1, 2], True),              # dup at edges
        ([9, 7, 8, 7, 6], True),        # duplicate in middle
        ([100, 200, 300], False),       # no duplicates, random numbers
        ([-1, -2, -3, -1], True),       # negative numbers with dup
        ([0, 1, 2, 3, 0], True)         # zero repeated
    ]

    for nums, expected in tests:
        result = sol.hasDuplicate(nums.copy())
        print(f"Input: {nums} → Output: {result} (Expected: {expected})")
