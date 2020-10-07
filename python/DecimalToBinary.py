def DecimalToBinary(x):
    BinaryNumb = '0' + bin(x)[2:]
    return BinaryNumb

def main():
    x = int(input("Enter Decimal Number: "))
    BinaryNumb = DecimalToBinary(x)
    print("Binary Number: ",BinaryNumb)
main()
