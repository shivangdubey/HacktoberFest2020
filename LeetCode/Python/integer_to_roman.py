class Solution:
    def intToRoman(self, num: int) -> str:

        """
        :type num: int
        :rtype: str
        """
        '''
        I can be placed before V (5) and X (10) to make 4 and 9.
        X can be placed before L (50) and C (100) to make 40 and 90.
        C can be placed before D (500) and M (1000) to make 400 and 900.
        '''

        dict = {
        1    : 'I',
        4    : 'IV',
        5    : 'V',
        9    : 'IX',
        10   : 'X',
        40   : 'XL',
        50   : 'L',
        90   : 'XC',
        100  : 'C',
        400  : 'CD',
        500  : 'D',
        900  : 'CM',
        1000 : 'M'}

        s = ''
        if num >= 1000:
            s += f'{dict.get(1000) *  (num //1000)}'
            num = num % 1000

        if num >= 900:
            s += f'{dict.get(900) *  (num //900)}'
            num = num % 900


        if num >= 500:
            s += f'{dict.get(500) *  (num //500)}'
            num = num % 500


        if num >= 400:
            s += f'{dict.get(400) *  (num //400)}'
            num = num % 400


        if num >= 100:
            s += f'{dict.get(100) *  (num //100)}'
            num = num % 100


        if num >= 90:
            s += f'{dict.get(90) *  (num //90)}'
            num = num % 90


        if num >= 50:
            s += f'{dict.get(50) *  (num //50)}'
            num = num % 50


        if num >= 40:
            s += f'{dict.get(40) *  (num //40)}'
            num = num % 40


        if num >= 10:
            s += f'{dict.get(10) *  (num //10)}'
            num = num % 10


        if num >= 9:
            s += f'{dict.get(9) *  (num //9)}'
            num = num % 9


        if num >= 5:
            s += f'{dict.get(5) *  (num //5)}'
            num = num % 5


        if num >= 4:
            s += f'{dict.get(4) *  (num //4)}'
            num = num % 4


        if num >= 1:
            s += f'{dict.get(1) *  (num //1)}'
            num = num % 1


        return s


if __name__ == '__main__':

    x = 16
    instance = Solution()
    solution = instance.intToRoman(x)
    # print('list: ', solution[0],'sum: ', solution[1] , 'new_list',  solution[2], sum(solution[2]))
    print(solution)
    #: print(type(solution))


dict = {
1    : 'I',
4    : 'IV',
5    : 'V',
9    : 'IX',
10   : 'X',
40   : 'XL',
50   : 'L',
90   : 'XC',
100  : 'C',
400  : 'L',
500  : 'CD',
900  : 'CM',
1000 : 'M'}
s = f'{dict.get(1000) *  (3994 //1000)}'

s






def romanToInt_faster(self, s: str) -> int:
    val_map = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}

    total = 0

    s = s.replace("IV", "IIII").replace("IX", "VIIII")
    s = s.replace("XL", "XXXX").replace("XC", "LXXXX")
    s = s.replace("CD", "CCCC").replace("CM", "DCCCC")

    for char in s:
        total += val_map[char]

    return total
