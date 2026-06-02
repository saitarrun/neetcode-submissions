class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        dicts = defaultdict(list)

        for i in strs:
            sortedS = ''.join(sorted(i))
            dicts[sortedS].append(i)
        return list(dicts.values())
        