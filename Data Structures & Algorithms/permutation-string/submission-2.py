class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1Dict = {}

        # init s1Dict
        for c in s1:
            prevCount = s1Dict.get(c, 0)
            s1Dict[c] = prevCount + 1

        i = 0
        while i < len(s2):
            if s1Dict.get(s2[i], 0) == 0:
                i += 1
                continue
            tempDict = s1Dict.copy()
            j = i

            while tempDict.get(s2[j], 0) != 0:
                prevCount = tempDict.get(s2[j])
                if prevCount == 1:
                    del tempDict[s2[j]]
                else:
                    tempDict[s2[j]] = prevCount - 1
                j += 1
                if j == len(s2):
                    break
            
            if not tempDict:
                return True
            i += 1
        
        return False