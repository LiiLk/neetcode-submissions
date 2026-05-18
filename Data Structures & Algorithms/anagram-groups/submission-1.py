class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        identity = {}
        for word in strs:
            key = "".join(sorted(word))
            if key not in identity:
                identity[key] = []
            identity[key].append(word)
        return list(identity.values())