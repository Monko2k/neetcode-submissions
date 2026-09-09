class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = {}
        for item in strs:
            key = ''.join(sorted(item))
            if key in groups:
                groups[key].append(item)
            else:
                groups[key] = [item]
        return list(groups.values())
        