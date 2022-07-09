"""
Перевод арабских чисел в римские.
"""

class Solution:

    def intToRoman(self, num: int) -> str:
        arab = {
            1000: 'M',
            900: 'CM',
            500: 'D',
            400: 'CD',
            100: 'C',
            90: 'XC',
            50: 'L',
            40: 'XL',
            10: 'X',
            9: 'IX',
            5: 'V',
            4: 'IV',
            1: 'I',
        }
        str_num = str(num)
        count = ''
        rank = 10 ** (len(str_num))
        for index, item in enumerate(str_num):
            dig = int(item)
            rank /= 10
            res = arab.get(dig * rank)
            if res:
                count += res
            elif dig < 5:
                count += arab.get(rank) * dig
            else:
                count += arab.get(5 * rank)
                count += arab.get(rank) * (dig - 5)

        return count


s = Solution()
test = [124, 643, 475, 34, 2, 3, 745, 432, 1994]

for i in test:
    print(f'{i:<4} -> {s.intToRoman(i)}')
