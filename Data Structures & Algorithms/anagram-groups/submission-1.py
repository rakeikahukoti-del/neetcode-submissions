from collections import defaultdict
from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = defaultdict(list)

        for word in strs:
            counts = [0] * 26

            for char in word:
                index = ord(char) - ord('a')
                counts[index] += 1

            # A tuple is immutable and can be used as a dictionary key
            signature = tuple(counts)
            groups[signature].append(word)

        return list(groups.values())