print("=========================")
print("      mi calculadora")
print("=========================")

while True:
    print("")
    print("¿qué operacion deseas realizar?")
    print("1. sumar")
    print("2. restar")
    print("3. salir")
    print("------------------")

    opcion = input("elige una opcion: ")

    if opcion == "1":
        num1 = input("ingresa el primer numero: ")
        num2 = int(num1)
        num2 = input("ingresa el segundo numero: ")
        num2 = int(num2)
        print("el resultado de la suma es:",num1+num2)

    elif opcion == "2":
        num1 = input("ingresa el primer numero: ")
        num2 = int(num1)
        num2 = input("ingresa el segundo numero: ")
        num2 = int(num2)
        print("el resustado de la resta es:",num1-num2)

    elif opcion == "3":
        print("¡gracias por usar mi calculadora¡")
        break

    else:
        print("opcion incorrecta.intenta nuevamente.")



        print("======================")
        print("          ¡hasta pronto¡")
        print("======================")
