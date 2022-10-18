from services.create_auto import createAuto
from services.read_auto import readCarByChassi
from services.remove_auto import removeAuto
from services.sale_auto import venderAuto
from services.update_value_auto import updateValueAuto

inicio = input("Podemos Iniciar o Programa?\nDigite 'S' para Sim, ou 'N' para Não: ").upper()

# Menu de ações
while(inicio == "S"):
    print('============================================================')
    print("Bem-Vindo ao Sistema AutoCar")
    print("Opções Disponíveis: ⤵ ")
    print("1 - Adicionar Automóvel")
    print("2 - Consultar Cadastro de Automóveis")
    print("3 - Remover Automóvel")
    print("4 - Alterar Valor do Automóvel")
    print("5 - Consultar Condições de Venda")
    print("6 - Sair")
    print('============================================================')
    solicitacao = input("Digite o Número da Opção Desejada: ").upper()

# Chamada das funções
    if (solicitacao == "1"):
        createAuto()

    elif (solicitacao == "2"):
        readCarByChassi()

    elif (solicitacao == "3"):
        removeAuto()

    elif (solicitacao == "4"):
        updateValueAuto()

    elif (solicitacao == "5"):
        venderAuto()

    elif (solicitacao == "6"):
        print('============================================================')
        print("Programa encerrado.")
        print('============================================================')
        break

else:
    if(inicio == "N"):
        print('============================================================')
        print("Programa encerrado.")
        print('============================================================')
    elif(inicio != "N" or "S"):
        print('============================================================')
        print("Digite uma opção válida.")
        print('============================================================')