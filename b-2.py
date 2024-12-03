by1 = input("行数を入力してください：")
by2 = input("列数を入力してください：")

for i in range(1, int(by1)+1):
    for j in range(1, int(by2)+1):
        print(i * j, end=" ")

    print()
