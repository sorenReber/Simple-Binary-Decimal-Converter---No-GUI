#Binary to Decimal Converter Version 2

def main():

    quantity = int(input("How many binary numbers do you wish to enter? "))
    while quantity > 4 or quantity <= 0:
        quantity = int(input("Please enter a number between 1 and 4: "))
    decimal = [0,0,0,0]
    for i in range(quantity):
        binary = input('Enter a number in binary: ')
        while len(binary) > 8:
            print(f'Please only enter 8 binary digits. You entered {len(binary)}')
            binary = input('Enter a number in binary: ')
        if len(binary) < 8:
            for _ in range(8 - len(binary)):
                binary += '0'
        print(binary)
        convert_decimal = bi_to_dec(binary)
        decimal[i] = convert_decimal

    print(f'The IP address would be {decimal[0]}.{decimal[1]}.{decimal[2]}.{decimal[3]}')

def bi_to_dec(binary):
    decimal = 0
    for i in range(len(binary)):
        if binary[i] == "1":
            decimal += 128 / (2 ** i)
        else:
            decimal += 0

    return f'{decimal:.0f}'

if __name__ == "__main__":
    main()
