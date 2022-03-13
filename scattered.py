
for j in range(24):
    n = pow(2, j)
    number_of_scattered = n
    for i in range(n):
        if "11" in format(i, "08b"):
            number_of_scattered -= 1


    print('There are {0} scattered numbers less than 2^{1}'.format(number_of_scattered, str(j)))