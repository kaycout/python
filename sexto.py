numero_placa = input("Digite o número final da placa do veículo: ")

match numero_placa:
    case "1" | "2": print ("Rodízio na segunda-feira")
    case "3" | "4": print ("Rodízio na terça-feira")
    case "5" | "6": print ("Rodízio na quarta-feira")
    case "7" | "8": print ("Rodízio na quinta-feira")
    case "9" | "0": print ("Rodízio na sexta-feira")
    case _: print("Final de placa inválido")

