def topKFrequent(self, nums: List[int], k: int) -> List[int]:
    # Count frequencies
    freq = {}
    for n in nums:
        freq[n] = freq.get(n, 0) + 1

    # Sort by frequency (highest first) and take first k
    sorted_items = sorted(freq.items(), key=lambda x: x[1], reverse=True)

    return [num for num, count in sorted_items[:k]]
