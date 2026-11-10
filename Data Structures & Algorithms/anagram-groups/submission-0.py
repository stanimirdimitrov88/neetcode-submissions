class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        output = []

        a = {}
        for index, string in enumerate(strs):
            new_word = []
            for l in string: 
                new_word.append(l)
                    
            new_word.sort()
            unique_letters = "".join(new_word)
            
            if unique_letters in a:
                a[unique_letters].append(string)
            else:
                a[unique_letters] = [string]

        for unique_letters, l in a.items(): 
            output.append(l)

        return output