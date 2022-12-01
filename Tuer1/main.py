import re

with open(r"C:\Users\u-77516\Desktop\new 29.txt", 'r') as ff:
    lines = ff.readlines()

sumList = []
sumItem = 0
for item in lines:
    if re.match(r'\d+', item):
        item = int(item.replace(r'\n', ''))
        sumItem += item
        continue

    sumList.append(sumItem)
    sumItem = 0

sumList.sort()


def GetHightestNumber():
    return max(sumList.copy())


def GetSumOfNHighest(n: int):
    return sum(sumList[-n:])


if __name__ == '__main__':
    print(GetHightestNumber())
    print(GetSumOfNHighest(3))
