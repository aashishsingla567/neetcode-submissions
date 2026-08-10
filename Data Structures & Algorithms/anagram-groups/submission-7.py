BIG = 1000000007

def get_hash(s: str):
    return ''.join(sorted(s))

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = dict()
            
        for s in strs:
            h = get_hash(s)
            
            if (d.get(h)):
                d[h].append(s)
            else:
                d[h] = [s]

        return list(d.values())
        