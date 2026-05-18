class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        identity = {}
        for word in strs:
            key = "".join(sorted(word))
            if key in identity:
                identity[key].append(word)
            else:
                identity[key] = []
                identity[key].append(word)
        return list(identity.values())