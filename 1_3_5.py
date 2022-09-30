def multBin(firstnumber, secondnumber):
    firstnumber = str(firstnumber)
    secondnumber = str(secondnumber)

    Multiplication = int(firstnumber, 2) * int(secondnumber, 2)
    binaryMul = str(bin(Multiplication))[2:]

    print("\nResult = " + binaryMul)

multBin(111,101)