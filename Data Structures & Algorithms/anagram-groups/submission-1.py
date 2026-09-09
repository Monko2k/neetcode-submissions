class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = defaultdict(list)
        for item in strs:
            freq = [0] * 26
            for c in item:
                letter = (ord(c) - ord('a'))
                freq[letter] += 1
            key = tuple(freq)
            groups[key].append(item)
        return list(groups.values())
        