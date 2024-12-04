import random


def dice():
    dice = random.randint(1, 6)
    return dice


print(dice())  # 1から6の整数をランダムに出力する
