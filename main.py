print("Banco Corresponsal")

operaciones = int(input("¿Cuantas operaciones desea realizar?: "))

for i in range(operaciones):
    selection= int(input("Seleccione la operacion deseada:\n1- Consultar saldo.\n2- Retirar.\n3- Depositar. \n Operación # {i + 1}: "))
