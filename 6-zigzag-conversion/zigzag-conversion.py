class Solution(object):
    def convert(self, s, num_rows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if num_rows == 1 or num_rows >= len(s):
            return s
        zigzag_string = [''] * num_rows
        row = 0
        step = 1

        for char in s:
            zigzag_string[row] += char
            row += step

            if row == 0:
                step = 1  
            if row == num_rows-1:
                step = -1  

        return "".join(zigzag_string)
        