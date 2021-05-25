import time
registro = {}
valor_hora = 4.50

while True:
    print("-= Registro de carros no estacionamento =-")
    opcao = int(input("1 - Registrar entrada\n2 - Consultar veículo\n3 - Registrar saída\n4 - Sair\n>> "))
    # Opção de saída
    if opcao == 4:
        break
    # Opção de Entrada de Registro
    elif opcao == 1:
        while True:
            placa_ent = input("Qual a placa do carro em entrada (Maiúsculo com traço)? ")
            if len(placa_ent) == 8:
                break
            else:
                print("Placa inválida. Tente novamente")
        agora_ent = time.localtime()
        horario_entrada = [agora_ent[3], agora_ent[4], agora_ent[5]]
        registro.update({str(placa_ent): horario_entrada})
    # Opção de consulta de veículos registrados
    elif opcao == 2:
        if registro == {}:
            for y in range(2):
                print()
            print("Sem Registros.")
            for y in range(2):
                print()
        else:
            for y in range(2):
                print()
            for linha in registro:
                print("----------------")
                print(f"Placa {linha} chegou às {registro[linha]}.")
                print("----------------")
                print()
    # Opção de Saída de Registro
    elif opcao == 3:
        while True:
            placa_sai = input("Qual placa do carro em saída? ")
            if len(placa_sai) == 8 and placa_sai in registro:
                break
            else:
                print("Placa inválida. Tente novamente.")
        agora_sai = time.localtime()
        horario_saida = [agora_sai[3], agora_sai[4], agora_sai[5]]
        aux = registro.get(placa_sai)
        diferenca_int = horario_saida[0] - aux[0]
        diferenca_par = horario_saida[1] - aux[1]
        valor = (diferenca_int * valor_hora) + (diferenca_par * valor_hora)
        registro.pop(placa_sai)
        print(f"Custo total de R${valor} reais.")
        print()
