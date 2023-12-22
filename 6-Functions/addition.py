def addition(a, b):
    return a + b

#Main program
def main():
    num1 = float(input('Enter the 1st number:\n'))
    num2 = float(input('Enter the 2nd number:\n'))

    res = addition(num1, num2)
    print('The result is', res)

main()