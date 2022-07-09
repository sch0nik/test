"""
Напишите функцию, которая находит самый длинный префикс, общий для всего массива строк.
Если его нет, вернуть пустую строку.


Пример 1:
Input: strs = ["flower","flow","flight"]
Output: "fl"

Пример 2:
Input: strs = ["dog","racecar","car"]
Output: ""

Объяснение: Среди входных строк нет общего префикса.
"""


def main(s):
    m = min(s, key=len)
    while m:
        for i in s:
            if not i.startswith(m):
                break
        else:
            return m
        m = m[:-1]
    return ''


if __name__ == '__main__':
    s1 = ['flower', 'flow', 'flight']
    s2 = ['dog', 'racecar', 'car']
    s3 = ['топор', 'топот', 'топонимика']

    print(f'{s1} --> {main(s1)}')
    print(f'{s2} --> {main(s2)}')
    print(f'{s3} --> {main(s3)}')
