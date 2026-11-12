class Solution:

    def encode(self, strs: List[str]) -> str:
        if strs == []: 
            return "asdonwneifownidnsdqwoidjq"

        string = "///".join(strs) 
        
        return string

    def decode(self, s: str) -> List[str]:
        if s == "asdonwneifownidnsdqwoidjq": 
            return [] 
    
        p = s.split("///")
        return p 