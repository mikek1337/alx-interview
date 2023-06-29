def pascal_triangle(n):
    pascal = []
    i = 0
    if (n <= 0):
        return []
    while (n > i):
        current_pascal = []
        new_pascal = []
        j = 0
        if (len(pascal) != 0):
            current_pascal = pascal[-1]
            print("Current pascal", end="")
            print(current_pascal)
        if (i == 0):
            new_pascal.append(1)
            pascal.append(new_pascal)
        while (len(current_pascal) > j):
            if (j == 0):
                new_pascal.append(1)
            if (len(current_pascal) - 1 == j):
                new_pascal.append(1)
            else:
                next_index = j + 1
                new_pascal.append(current_pascal[j] + current_pascal[next_index])
            pascal.append(new_pascal)
            j += 1
        i += 1
    print("Final pascal", end="")
    print(pascal)
    return pascal
