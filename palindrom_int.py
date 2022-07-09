"""
Вернуть true, если x является целым палиндромом.
Целое число является палиндромом, если оно читается так же, как в прямом, так и в обратном порядке.
Например, 121 — это палиндром, а 123 — нет.

Input: x = 121
Output: true
Explanation: 121 reads as 121 from left to right and from right to left.
"""


def main(x):
    s = str(x)
    l = int(len(s)/2)
    return s[:l] == s[-1: -l - 1: -1]


if __name__ == '__main__':
    l = [123, 535, 3456543]
    for i in l:
        print(f'{i:<8} --> {main(i)}')
