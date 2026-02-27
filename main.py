elif selection == 3:
        deposito = int(input("¿Cuánto desea depositar?: "))
        while deposito <= 0:
            print("Por favor ingrese un depósito válido")
            deposito = int(input("¿Cuánto desea depositar?: "))

        saldo += deposito
        print("Su nuevo saldo es:", saldo)

    else:
        print("Opción no válida")
