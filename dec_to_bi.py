def main():

    decimal_input = int(input('Enter a decimal number to convert to binary: '))
    binary = dec_to_bi(decimal_input)

    print(binary)

def dec_to_bi(dec):
    add_to_binary = ''
    decimal = dec

    for i in range(7,-1,-1):
        if decimal >= (2 ** i):
            add_to_binary += '1'
            decimal = decimal - (2 ** i)
        else:
            add_to_binary += '0'
    return add_to_binary

if __name__ == "__main__":
    main()