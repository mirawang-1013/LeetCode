class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        group = defaultdict(list) #dict
        for i in strs:
            key= "".join(sorted(i))
            group[key].append(i)
        return list(group.values())

























        # output=defaultdict(list)
        # for i in strs:
        #     output[tuple(sorted(i))].append(i)
        # return list(output.values())

