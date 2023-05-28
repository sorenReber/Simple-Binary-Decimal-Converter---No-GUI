from bi_to_dec import bi_to_dec
from dec_to_bi import dec_to_bi

def main():
    the_loop = -1
    print('What are you looking to convert from today?')
    while the_loop == -1:
        answer = input("Please enter decimal, binary or exit to quit: ")
        answer = answer.lower()
        if answer == 'exit':
            
            break

        if answer == 'decimal':

            decimal_input = int(input('Enter a decimal number to convert to binary: '))
            binary_converted = dec_to_bi(decimal_input)
            print(f'The binary version of {decimal_input} is: {binary_converted}')

        elif answer == 'binary':

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

        else:

            print(f"I'm sorry but {answer} was not one of the options.")




if __name__ == "__main__":
    main()