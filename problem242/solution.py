# My thoughts----
# 1. length(s) == length(t)
# 2. length(unique(s)) == length(unique(t))
# 3. Each unique(s) is in unique(t)

# solution---
class Solution:
    def __init__(self) -> None:
        pass

    def is_anagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

obj1 = Solution()
# print(obj1.is_anagram(s="Mwavu", t="mbiti"))
print(Solution().is_anagram(s="Mwavu", t="mbiti"))