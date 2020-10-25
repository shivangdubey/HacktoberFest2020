class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
		
		# generate column-wise slicing
        column_slices, common_prefix = zip(*strs), ''
        
        for current_column in column_slices:
            
            if len(set(current_column)) == 1:
				# current column-wise slice's character is the same
				# update common prefix
                common_prefix += current_column[0]
            
            else:
				# current column-wise slice's character is different
                break
                
        return common_prefix
