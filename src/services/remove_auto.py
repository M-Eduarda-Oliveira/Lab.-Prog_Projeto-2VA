from data.registration_car import registrationsCar
from utils.show_messages import showMessage

def removeAuto():
  chassi = input("Digite o chassi do Automóvel que deseja remover: ")

  if registrationsCar.get(chassi):
    registrationsCar.pop(chassi, None)
    showMessage("Automóvel Removido com Sucesso.")
    return
  else:
    showMessage(f'Não temos cadastro de Automóvel com este Chassi:', chassi)
    return
