class Solution:
    def removeComments(self, s: List[str]) -> List[str]:
        # join the whole array in to a string by -
        # iterate over it 
           # if we get // remove till that indexed array
           # if we get /* remove till */ 
      
        return [*filter(None,re.sub('//.*|/\*(.|\n)*?\*/','','\n'.join(s)).split('\n'))]



        

