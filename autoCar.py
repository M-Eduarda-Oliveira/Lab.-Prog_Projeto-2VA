cadastroDeAutos = {
"9BWZZZ377VT004251":["ONIX","CHEVROLET","2015",40000,"PRATA","MANUAL"],
"9BWZZZ377VT004252":["FOX","VOLKSWAGEN","2012",25000,"PRETO","MANUAL"],
"9BWZZZ377VT004253":["ECOSPORT","FORD","2016",55000,"BRANCO","MANUAL"],
"9BWZZZ377VT004254":["CIVIC","HONDA","2017",75000,"PRETO","AUTOMÁTICO"],
"9BWZZZ377VT004255":["UNO","FIAT","2014",35000,"VERMELHO","MANUAL"],
"9BWZZZ377VT004256":["307","PEUGEOT","2018",43000,"BRANCO","AUTOMÁTICO"],
"9BWZZZ377VT004257":["SANDERO","RENAULT","2019",40000,"AZUL","MANUAL"],
"9BWZZZ377VT004258":["GOLF","VOLKSWAGEN","2020",95000,"BRANCO","AUTOMÁTICO"],
"9BWZZZ377VT004259":["FUSION","FORD","2021",120000,"BRANCO","AUTOMÁTICO"],
}

inicio = input(
    "Podemos Iniciar o Programa?\nDigite 'S' para Sim, ou 'N' para Não: ").upper()

# Menu de ações
while(inicio == "S"):
    print('============================================================')
    print("Bem-Vindo ao Sistema AutoCar")
    print("Opções Disponíveis: ⤵ ")
    print("01 - Adicionar Automóvel")
    print("02 - Consultar Cadastro de Automóveis")
    print("03 - Remover Automóvel")
    print("04 - Alterar Valor do Automóvel")
    print("05 - Consultar Condições de Venda")
    print("06 - Sair")
    print('============================================================')
    solicitacao = input("Digite o Número da Opção Desejada: ").upper()

# Função de adicionar/cadastrar automóvel


    def addAuto():
        chassi = input("Digite o Chassi do Automóvel: ")
        if len(chassi) == 17:
            if cadastroDeAutos.get(chassi):
                print('============================================================')
                print("Já temos um automóvel cadastrado com este chassi:", chassi)
                print('============================================================')
                return
            
            else:
                modelo = input("Digite o Modelo do Automóvel: ")
                marca = input("Digite o Fabricante do Automóvel: ")
                ano = input("Digite o Ano do Automóvel: ")
                valor = float(input("Digite o Valor do Automóvel (R$): "))
                cor = input("Digite a Cor do Automóvel: ")
                cambio = input("Digite o tipo de Câmbio do Automóvel: ")
                cadastroDeAutos[chassi] = [modelo, marca, ano, valor, cor, cambio]
                print('============================================================')
                print("Automóvel Cadastrado com Sucesso!")
                print('============================================================')
                return
        elif (len(chassi) > 17) or (len(chassi) < 17):
            if chassi == "0":
                print("Voltando para o Menu...")
                return
            else:
                print("Digite uma númeração de chassi válida!")
                return addAuto()          

# Função para Automóveis já cadastrados
    def consultCad():
        chassi = input("Digite o Chassi Cadastrado: ")

        if cadastroDeAutos.get(chassi):
            print("==================AUTOMÓVEL CADASTRADO======================")
            print("Chassi:",chassi)
            print("Modelo:",cadastroDeAutos[chassi][0])
            print("Fabricante:",cadastroDeAutos[chassi][1])
            print("Ano:",cadastroDeAutos[chassi][2])
            print(f'Valor: R$ {real(cadastroDeAutos[chassi][3])}')
            print("Cor:",cadastroDeAutos[chassi][4])
            print("Câmbio:",cadastroDeAutos[chassi][5])
            print('============================================================')
        else:
            print('============================================================')
            print(f'Não temos cadastro de Automóvel com este Chassi:',chassi)
            print('============================================================')
            return

# Função para formatar saída em valor monetário (R$)
    def real(valor):
            a = "{:,.2f}".format(float(valor))
            b = a.replace(',', 'v')
            c = b.replace('.', ',')
            return c.replace('v', '.')

# Função para remover um automóvel do sistema de cadastro
    def removeAuto():
        chassi = input("Digite o chassi do Automóvel que deseja remover: ")

        if cadastroDeAutos.get(chassi):
            cadastroDeAutos.pop(chassi, None)
            print('============================================================')
            print("Automóvel Removido com Sucesso.")
            print('============================================================')
            return
        else:
            print('============================================================')
            print(f'Não temos cadastro de Automóvel com este Chassi:',chassi)
            print('============================================================')
            return

# Função para Atualizar Valor do Automóvel
    def cadNovoValor():
        chassi = input("Digite o chassi do Automóvel: ")
        novoValor = float(input("Digite o Novo Valor do Automóvel: "))
        cadastroDeAutos[chassi][3] = novoValor
        print(f'O Novo Valor foi Cadastrado: R$ {real(cadastroDeAutos[chassi][3])}')

# Função para iniciar Venda do Automóvel
    def venderAuto():
        chassi = input("Digite o chassi do Automóvel para Iniciar a Venda: ")
        if chassi in cadastroDeAutos:
            print("Escolha a Opção de Pagamento")
            print("01 - Á Vista")
            print("02 - Parcelado")
            formaDePagamento = input("Digite o Metódo de Pagamento: ")
            if (formaDePagamento == "1" or formaDePagamento == "01"):
                # O valor original do produto
                valorOriginal = cadastroDeAutos[chassi][3]
                # Desconto que será concedido
                desconto = float(input("Desconto (em %) para esse Automóvel: "))
                # Transformando a porcentagem em número decimal
                desconto = desconto / 100
                # Exibindo os Resultados
                print(f'Valor original: R$ {real(valorOriginal)}')
                print(f'Desconto ganho: R$ {real(valorOriginal * desconto)}')
                print(f'Valor com desconto: R$ {real(valorOriginal * (1-desconto))}')

            elif (formaDePagamento == "2" or formaDePagamento == "02"):
                print('============================================================')
                print("Escolha a Opção de Parcelamento: ⤵")
                print("01 - 12x")
                print("02 - 24x")
                print("03 - 36x")
                print("04 - 48x")
                print('============================================================')
                valorOriginal = cadastroDeAutos[chassi][3]
                meses = input("Digite a Opção Escolhida: ")

                if (meses == "1" or meses == "01"):
                    juros = 0.05
                    meses = 12
                    print('============================================================')
                    print(f'O Valor do Automóvel é: R$ {real(valorOriginal)}')
                    print(f'O Valor Total do Automóvel Parcelado em 12x é: R$ {real(valorOriginal + (valorOriginal * juros))} considerando juros de {(juros * 100)}% ao mês.')
                    print(f'Com Parcelas de R$ {real((valorOriginal + (valorOriginal * juros)) / meses)} ao mês')
                    print('============================================================')
                elif (meses == "2" or meses == "02"):
                    juros = 0.06
                    meses = 24
                    print('============================================================')
                    print(f'O Valor do Automóvel é: R$ {real(valorOriginal)}')
                    print(f'O Valor Total do Automóvel Parcelado em 24x é: R$ {real(valorOriginal + (valorOriginal * juros))} considerando juros de {(juros * 100)}% ao mês.')
                    print(f'Com Parcelas de R$: R$ {real((valorOriginal + (valorOriginal * juros)) / meses)} ao mês')
                    print('============================================================')
                elif (meses == "3" or meses == "03"):
                    juros = 0.07
                    meses = 36
                    print('============================================================')
                    print(f'O Valor do Automóvel é: R$ {real(valorOriginal)}')
                    print(f'O Valor Total do Automóvel Parcelado em 36x é: R$ {real(valorOriginal + (valorOriginal * juros))} considerando juros de {(juros * 100)}% ao mês.')
                    print(f'Com Parcelas de R$: R$ {real((valorOriginal + (valorOriginal * juros)) / meses)} ao mês')
                    print('============================================================')
                elif (meses == "4" or meses == "04"):
                    juros = 0.08
                    meses = 48
                    print('============================================================')
                    print(f'O Valor do Automóvel é: R$ {real(valorOriginal)}')
                    print(f'O Valor Total do Automóvel Parcelado em 48x é: R$ {real(valorOriginal + (valorOriginal * juros))} considerando juros de {(juros * 100)}% ao mês.')
                    print(f'Com Parcelas de R$: R$ {real((valorOriginal + (valorOriginal * juros)) / meses)} ao mês')
                    print('============================================================')
                else:
                    print('============================================================')
                    print(f"Digite uma opção válida.")
                    print('============================================================')

        else:
            print('============================================================')
            print(f'Não temos cadastro de Automóvel com este Chassi:', chassi)
            print('============================================================')

# Chamada das funções
    if (solicitacao == "1" or solicitacao == "01"):
        addAuto()

    elif (solicitacao == "2" or solicitacao == "02"):
        consultCad()

    elif (solicitacao == "3" or solicitacao == "03"):
        removeAuto()

    elif (solicitacao == "4" or solicitacao == "04"):
        cadNovoValor()

    elif (solicitacao == "5" or solicitacao == "05"):
        venderAuto()

    elif (solicitacao == "6" or solicitacao == "06"):
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