repeat = True
while repeat == True: 

    num = int(input("Name a number from 1 to 1000 \n"))

    while num<1 or num>1000:
        print("That number is not in the range.\nGive me another one please")
        num = int(input("Tell me another number, which is between 1 and 1000, it is worth 1 and 1000.\n"))

    resultado = num % 2

    if resultado == 0:
        print("The number " + str(num) + " is even")
    else:
        print("The number " + str(num) + " is odd")
    
    respuesta = str(input("Do you want to play again? Yes/No\n"))

    if respuesta == "yes" or respuesta == "Yes" or respuesta == "YES":
        repeat = True
    else:
        repeat = False
