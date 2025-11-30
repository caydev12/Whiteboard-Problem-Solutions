class Solution:
    def topKFrequent(self, nums, k):
        # Count frequencies
        freq = {}
        for n in nums:
            freq[n] = freq.get(n, 0) + 1

        # Sort by frequency (highest first) and take first k
        sorted_items = sorted(freq.items(), key=lambda x: x[1], reverse=True)

        return [num for num, count in sorted_items[:k]]

if __name__ == "__main__":
    sol = Solution()

    tests = [
        # (nums, k, expected_output)
        ([1,1,1,2,2,3], 2, [1,2]),        # typical case
        ([1], 1, [1]),                    # single element
        ([4,4,4,4], 1, [4]),              # all same
        ([1,2,3,4], 1, [1,2,3,4]),        # any order acceptable; all freq=1
        ([1,2,2,3,3,3], 2, [3,2]),        # descending frequency
        ([5,6,5,6,7], 3, [5,6,7]),        # k = all unique values
        ([10,10,20,20,20,30], 1, [20]),   # one clear most frequent
        ([], 0, []),                      # edge case: empty list
        ([1,2,3,1,2,1], 1, [1]),          # one dominant frequency
        ([0,0,0,1,1,2], 2, [0,1]),        # zero included
    ]

    for nums, k, expected in tests:
        result = sol.topKFrequent(nums.copy(), k)
        print(f"Input: nums={nums}, k={k} → Output: {result} (Expected: {expected})")
