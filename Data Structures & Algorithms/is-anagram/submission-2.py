class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hash={}

        for char in s:
            hash[char]= hash.get(char,0) +1
        
        for char in t:
            hash[char] = hash.get(char,0)-1

        return all(v==0 for v in hash.values())

