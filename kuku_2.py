number1 = int(input("数字入れて"))
number2 = int(input("数字入れて"))

for i in range(1, number1 + 1):
    for j in range(1, number2 + 1):
        answer = i * j
        print(f"{answer}", end=" ")
    print()
