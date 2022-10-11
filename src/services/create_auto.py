# Função de adicionar/cadastrar automóvel
from data.registration_car import registrationsCar
from utils.show_messages import showMessage

def createAuto():
    chassi = input("Digite o Chassi do Automóvel: ")[:17]

    if len(chassi) == 17:
        if registrationsCar.get(chassi):
            showMessage(
                "Já temos um automóvel cadastrado com este chassi:", chassi)
            return

        else:
            modelo = input("Digite o Modelo do Automóvel: ")
            marca = input("Digite o Fabricante do Automóvel: ")
            ano = input("Digite o Ano do Automóvel: ")
            valor = float(input("Digite o Valor do Automóvel (R$): "))
            cor = input("Digite a Cor do Automóvel: ")
            cambio = input("Digite o tipo de Câmbio do Automóvel: ")
            registrationsCar[chassi] = [
                modelo, marca, ano, valor, cor, cambio]
            showMessage("Automóvel Cadastrado com Sucesso!")
            return

    elif (len(chassi) > 17) or (len(chassi) < 17):
        if chassi == "0":
            print("Voltando para o Menu...")
            return
        else:
            print("Digite uma númeração de chassi válida!")
            return createAuto()
