def pattern(num):
    for i in range(0, num):
        for j in range(num, i, -1):
            print("* ", end="")
        print()

pattern(5)