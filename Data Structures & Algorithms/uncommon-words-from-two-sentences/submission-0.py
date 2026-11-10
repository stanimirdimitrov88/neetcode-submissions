class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        
        
        words_s1 = s1.split()
        words_s2 = s2.split()

        all_words = words_s1 + words_s2
        
        # create empty dict
        all_words_dict = {} 
        set_all_words = set(all_words)
        for i, k in enumerate(set_all_words): 
            all_words_dict[k] = 0            
        

        for i, k in enumerate(all_words):
            all_words_dict[k] = all_words_dict[k] + 1
        
        output = []
        for i, k in enumerate(all_words_dict): 
            if all_words_dict[k] == 1:
                output.append(k)

        return output
