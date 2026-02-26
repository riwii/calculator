elif selection == "2":
    while True:
        monto = float(input("Ingrese el monto a retirar: ")) 

        while monto <0: 
            print ("monto invalido: ")
            monto = float(input ("ingrese monto a retirar: "))

        if monto > saldo_inicial: 
                print ("saldo insuficiente")

        
    
