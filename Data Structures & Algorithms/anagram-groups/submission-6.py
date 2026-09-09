class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        def hash(string):
            key = [0] * 26
            for c in string:
                key[ord(c) - 97] += 1
            return tuple(key)


        cache = {}
        for s in strs:
            key = hash(s)
            if key in cache:
                cache[key].append(s)
            else:
                cache[key] = [s]
        
        return [s for s in cache.values()]



        