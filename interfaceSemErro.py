import PySimpleGUI as sg

# Layouts
def janelaInicio():
    layout = [
        [sg.Text('Deseja iniciar o programa?')],
        [sg.Button('Sim'), sg.Button('Não')],
    ]
    return sg.Window('inicio', layout=layout, finalize=True)


def janelaMenu():
    layout = [
        [sg.Text('''Seja bem-vindo!
        Escolha a opção desejada no nosso menu:''')],
        [sg.Button('1 - Adicionar automóvel')],
        [sg.Button('2 - Consultar cadastro de automóveis')],
        [sg.Button('3 - Remover automóvel')],
        [sg.Button('4 - Alterar valor do automóvel')],
        [sg.Button('5 - Consultar condições de venda')],
        [sg.Button('6 - Sair')],
    ]
    return sg.Window('Menu', layout=layout, finalize=True)


def janelaAdicAuto():
    layout = [
        [sg.Text("Digite o Chassi do Automóvel: ")],
        [sg.InputText(key="inputChassi")],
        [sg.Text("Digite o Modelo do Automóvel: ")],
        [sg.InputText(key="inputModelo")],
        [sg.Text("Digite o Fabricante do Automóvel: ")],
        [sg.InputText(key="inputFabricante")],
        [sg.Text("Digite o Ano do Automóvel: ")],
        [sg.InputText(key="inputAno")],
        [sg.Text("Digite o Valor do Automóvel (R$): ")],
        [sg.InputText(key="inputValor")],
        [sg.Text("Digite a Cor do Automóvel: ")],
        [sg.InputText(key="inputCor")],
        [sg.Text("Digite o tipo de Câmbio do Automóvel: ")],
        [sg.InputText(key="inputCambio")],
        [sg.Button('Adicionar'), sg.Button('Voltar')],
    ]
    return sg.Window('Adicionar Auto', layout=layout, finalize=True)

def consultarCadsAuto():
    layout = [
        [sg.Text("Chassi: ")],
        [sg.InputText(key="inputChassiCads")],
        [sg.Text("Modelo: ")],
        [sg.InputText(key="inputModeloCads")],
        [sg.Text("Fabricante: ")],
        [sg.InputText(key="inputFabricanteCads")],
        [sg.Text("Ano: ")],
        [sg.InputText(key="inputAnoCads")],
        [sg.Text("Valor(R$): ")],
        [sg.InputText(key="inputValorCads")],
        [sg.Text("Cor: ")],
        [sg.InputText(key="inputCorCads")],
        [sg.Text("Câmbio: ")],
        [sg.InputText(key="inputCambioCads")],
        [sg.Button('Consultar'), sg.Button('Voltar')],
    ]
    return sg.Window('Consultar Cadastro', layout=layout, finalize=True)

def removerAuto():
    layout =[
        [sg.Text("Digite o chassi do Automóvel que deseja remover: ")],
        [sg.InputText(key="InputChassiRemove")],
        [sg.Button('Remover'), sg.Button('Voltar')],
    ]
    return sg.Window('Remover Auto', layout=layout, finalize=True)

def mudarValor():
    layout = [
        [sg.Text("Digite o chassi do Automóvel que deseja modificar o valor: ")],
        [sg.InputText(key="InputChassiMudValor")],
        [sg.Text("Digite o novo valor do automóvel: ")],
        [sg.InputText(key="InputNovoValor")],
        [sg.Button('Modificar valor'), sg.Button('Voltar')],
    ]
    return sg.Window('Modificar Valor do Automóvel', layout=layout, finalize=True)

def venderAuto():
    layout = [
        [sg.Text("Digite o chassi do automóvel para iniciar a venda: ")],
        [sg.InputText(key="InputChassiVenda")],
        [sg.Button('Á vista'), sg.Button('Parcelado'), sg.Button('Voltar')],
    ]
    return sg.Window('Vender Automóvel', layout=layout, finalize=True)


def vendaAVista():
    layout = [
        [sg.Text("Venda à vista")],
        [sg.Text("Desconto em % para esse automóvel: ")],
        [sg.InputText(key="InputDescontoAuto")],
        [sg.Text("Valor original:"), sg.Text("", key="textoValorOriginal")],
        [sg.Text("Desconto ganho:"), sg.Text("", key="textoDesconto")],
        [sg.Text("Valor com desconto: R$"), sg.Text(
            "", key="textoValorComDesconto")],
        [sg.Button('Voltar'), sg.Button('Comprar')]
    ]
    return sg.Window('Venda à vista', layout=layout, finalize=True)


def vendaParcelado():
    layout = [
        [sg.Text("Venda à vista")],
        [sg.Text("Desconto em % para esse automóvel: ")],
        [sg.InputText(key="InputDescontoAuto")],
        [sg.Text("Valor original:"), sg.Text("", key="textoValorOriginal")],
        [sg.Text("Valor original:"), sg.Text("", key="textoDesconto")],
        [sg.Text("Valor original:"), sg.Text("", key="textoValorComDesconto")],
        [sg.Button('Ok')]
    ]
    return sg.Window('Venda à vista', layout=layout, finalize=True)

janelaInit, janelaEscolha, janelaAdd, janelaVeriCads, janelaExcluirAuto, janelaMudarValor, janelaVenda, janelaAvista, janelaParcelado= janelaInicio(), None, None, None, None, None, None, None, None

#Leitura dos eventos 
while True:
    window,event,values=sg.read_all_windows()
    #Quando a janela for fechada
    if window == janelaInit and event == sg.WIN_CLOSED or event == 'Não':
        break
    #Iniciar programa e fechar janela de inicio. Mostrar janela de menu.
    if window == janelaInit and event == 'Sim':
        janelaInit.close()
        janelaEscolha = janelaMenu()

    # Ifs da janela de menu:
    #Sair do programa a partir da janela de menu
    if window == janelaEscolha and event == '6 - Sair':
        break
    #Esconder janela de menu e mostrar janela de adicionar auto
    if window == janelaEscolha and event == '1 - Adicionar automóvel':
        janelaEscolha.hide()
        janelaAdd = janelaAdicAuto()
    # Abrir janela que verifica se o automóvel já foi cadastrado
    if window == janelaEscolha and event == '2 - Consultar cadastro de automóveis':
        janelaEscolha.hide()
        janelaVeriCads = consultarCadsAuto()
    # Abrir janela de remover automóvel 
    if window == janelaEscolha and event == '3 - Remover automóvel':
        janelaEscolha.hide()
        janelaExcluirAuto = removerAuto()
    # Abrir janela de modificar valor do automóvel
    if window == janelaEscolha and event == '4 - Alterar valor do automóvel':
        janelaEscolha.hide()
        janelaMudarValor = mudarValor()

# Funções dos botões da tela:
    # Ifs da janela de adicionar automóvel:
    # Voltar para o menu
    if window == janelaAdd and event == 'Voltar':
        janelaAdd.close()
        janelaEscolha.un_hide()
        # integração com código de adicionar auto
    if window == janelaAdd and event == 'Adicionar':
        sg.popup("Automóvel adicionado!")

    # Ifs da janela de cadastrar automóvel:
    # Voltar para o menu
    if window == janelaVeriCads and event == 'Voltar':
        janelaVeriCads.close() 
        janelaEscolha.un_hide()
        # integração com código de consultar cadastro de automóvel
    if window == janelaVeriCads and event == 'Consultar':
        sg.popup("Automóvel encontrado!")
    
    # Ifs da remoção de automóvel 
    # Voltar para o menu 
    if window == janelaExcluirAuto and event == 'Voltar':
        janelaExcluirAuto.close() 
        janelaEscolha.un_hide()
        # integração com código de remoção de automóvel
    if window == janelaExcluirAuto and event == 'Remover':
        sg.popup("Automóvel removido!")
    
    # Ifs de alterar valor de automóvel 
    # Voltar para o menu
    if window == janelaMudarValor and event == 'Voltar':
        janelaMudarValor.close() 
        janelaEscolha.un_hide()
    if window == janelaMudarValor and event == 'Modificar valor':
        sg.popup("Automóvel com valor modificado!")

    # Ifs Janela de Venda
    # voltar para o menu
    if window == janelaVenda and event == 'Voltar':
        janelaVenda.close() 
        janelaEscolha.un_hide()
    if window == janelaEscolha and event == '5 - Consultar condições de venda':
        janelaEscolha.hide()
        janelaVenda = venderAuto()