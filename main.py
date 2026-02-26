    if selection == 3:
        deposito = int(input("¿cuanto desea depositar?: "))
        while (deposito <= 0):
            print("Por favor ingrese un deposito válido")
            deposito = int(input("¿cuanto desea depositar?: "))
        saldo=  saldo + deposito
        print("Su nuevo saldo es: ", saldo)
