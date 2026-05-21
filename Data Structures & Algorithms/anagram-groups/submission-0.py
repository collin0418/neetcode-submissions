class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashMap=defaultdict(list)

        for n in strs:
            
            hashMap[''.join(sorted(n))].append(n)
        return list(hashMap.values())