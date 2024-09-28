class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        citations.sort(reverse=True)
        
        h_index = 0
        for i in range(len(citations)):
            citation = citations[i]  

            if citation >= i + 1:
                h_index = i + 1
            
        
        return h_index
        