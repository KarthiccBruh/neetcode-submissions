class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams=defaultdict(list)
        for item in strs:
            alphas=[0]*26
            for c in item:
                alphas[ord(c)-ord('a')]+=1
            key=tuple(alphas)
            anagrams[key].append(item)
        return list(anagrams.values())