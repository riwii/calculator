elif selection == 2:
        while True:
            monto = float(input("Ingrese el monto a retirar: "))

            if monto < 0:
                print("Monto inválido")
            elif monto > saldo:
                print("Saldo insuficiente")
            else:
                saldo -= monto
                print("Retiro exitoso")
                print(f"Nuevo saldo: {saldo}")
                break
