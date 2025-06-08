class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        group_anagrams = defaultdict(list)
        for i in strs:
            terms = ''.join(sorted(i))
            group_anagrams[terms].append(i)
        return list(group_anagrams.values())
        


