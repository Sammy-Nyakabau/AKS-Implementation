p = int(input("Enter a number: "))

def expand_x_1(p):
    if p == 1:
        print('Neither composite nor prime')
        exit()
    elif p < 1 or (p - int(p)) != 0:
        print('Invalid Input')
        exit()

    coefficient = [1]
    for i in range(p):
        coefficient.append(coefficient[-1] * -(p - i) / (i + 1))
    coefficients = coefficient[1: p]
    #print(coefficients)

    sum = 0  # Finding the sum of all the numbers in the coefficients
    for number in coefficients:
        int_value = int(number)
        abs_number = abs(int_value)
        #print(abs_number)
        sum += abs_number
    #print("Sum:",sum)

    if sum % p == 0:           # checking whether the number is prime or not
        print("{} is a prime".format(p))
    else:
        print("{} is not a prime".format(p))


expand_x_1(p)