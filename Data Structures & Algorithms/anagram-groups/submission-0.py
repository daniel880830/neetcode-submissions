class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = {}

        for voc in strs:
            key = "".join(sorted(voc))
            if key not in groups:
                groups[key] = []
            groups[key].append(voc)
            
        return list(groups.values())