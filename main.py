saldo=1000
print("Banco Corresponsal")

operaciones = int(input("¿Cuantas operaciones desea realizar?: "))

for i in range(operaciones):
    selection= int(input(f"Seleccione la operacion deseada:\n1- Consultar saldo.\n2- Retirar.\n3- Depositar. \nOperacion #{i + 1}: "))
    if selection == 1:
        print (f"el saldo actual: {saldo}")
    elif selection == 2:
        while True:
            monto = int(input("Ingrese el monto a retirar: "))

            if monto <= 0:
                print("Monto inválido")
            elif monto > saldo:
                print("Saldo insuficiente")
            else:
                saldo -= monto
                print("Retiro exitoso")
                print(f"Nuevo saldo: {saldo}")
                break
