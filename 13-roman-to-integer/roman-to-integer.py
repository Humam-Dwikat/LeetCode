class Solution(object):
    def convert_string_to_integer(self,r):
        roman_values = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
        }
        return roman_values.get(r, "not Found")

    def romanToInt(self, num):
        """
        :type num: str
        :rtype: int
        """
        result = 0
        i = 0

        while i < len(num):
            number1 = self.convert_string_to_integer(num[i])

            if i + 1 < len(num):
                number2 = self.convert_string_to_integer(num[i + 1])

                if number1 >= number2:
                    result += number1
                    i += 1
                else:
                    result += (number2 - number1)
                    i += 2
            else:
                result += number1
                i += 1

        return result
