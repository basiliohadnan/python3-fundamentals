def remainder_division(a, b):
    if b == 0:
        raise Exception('Divisor cannot be 0!')
    
    result = a // b
    remainder = a % b
    print(a, '/', b, 'is', result, 'and the remainder is', remainder)

#Main program
def main():
    remainder_division(10, 0)

main()
