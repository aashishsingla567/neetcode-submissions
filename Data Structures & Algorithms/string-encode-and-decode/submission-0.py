class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for x in strs:
            res += x + "/"
        return res

    def decode(self, s: str) -> List[str]:
        res = []
        
        part = ""
        for l in s:
            if l == "/":
                res.append(part)
                part = ""
                continue
            part += l
        return res