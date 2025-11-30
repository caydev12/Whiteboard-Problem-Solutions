class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        count = {}

        for c in s:
            count[c] = count.get(c, 0) + 1

        for c in t:
            if c not in count:
                return False
            count[c] -= 1
            if count[c] < 0:
                return False

        return True


if __name__ == "__main__":
    sol = Solution()

    tests = [
        ("anagram", "nagaram", True),       # typical anagram
        ("rat", "car", False),              # not an anagram
        ("a", "a", True),                   # single character match
        ("a", "b", False),                  # single character mismatch
        ("listen", "silent", True),         # common example
        ("", "", True),                     # both empty strings
        ("abc", "ab", False),               # different lengths
        ("aaab", "abaa", True),             # repeated characters
        ("hello", "bello", False),          # mismatch
        ("夜空", "空夜", True),              # unicode characters
    ]

    for s, t, expected in tests:
        result = sol.isAnagram(s, t)
        print(f"Input: s='{s}', t='{t}' → Output: {result} (Expected: {expected})")
