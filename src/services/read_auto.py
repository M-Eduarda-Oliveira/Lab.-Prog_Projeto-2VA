from data.registration_car import registrationsCar
from utils.show_messages import showMessage
from utils.format_BRL import formatBRL

def readCarByChassi():
  chassi = input("Digite o Chassi Cadastrado: ")

  if registrationsCar.get(chassi):
    print("==================AUTOMÓVEL CADASTRADO======================")
    print("Chassi:", chassi)
    print("Modelo:", registrationsCar[chassi][0])
    print("Fabricante:", registrationsCar[chassi][1])
    print("Ano:", registrationsCar[chassi][2])
    print(f'Valor: R$ {formatBRL(registrationsCar[chassi][3])}')
    print("Cor:", registrationsCar[chassi][4])
    print("Câmbio:", registrationsCar[chassi][5])
    print('============================================================')
    return
  else:
    showMessage('Não temos cadastro de Automóvel com este Chassi:', chassi)
    return
