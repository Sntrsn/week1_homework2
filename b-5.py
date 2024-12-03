def main():
    data = input("データを入力してください(スペース区切り) > ")
    numbers = list(map(int, data.split()))  # 入力を整数のリストに変換

    print(f"合計値: {cal_sum(numbers)}")
    print(f"最大値: {cal_max(numbers)}")
    print(f"最小値: {cal_min(numbers)}")
    print(f"平均値: {cal_mean(numbers)}")


def cal_sum(numbers):
    total = 0
    for num in numbers:
        total += num
    return total


def cal_max(numbers):
    max_value = numbers[0]
    for num in numbers:
        if num > max_value:
            max_value = num
    return max_value


def cal_min(numbers):
    min_value = numbers[0]
    for num in numbers:
        if num < min_value:
            min_value = num
    return min_value


def cal_mean(numbers):
    total = cal_sum(numbers)
    count = 0
    for _ in numbers:
        count += 1
    return total // count  # 整数値として計算


if __name__ == "__main__":
    main()
