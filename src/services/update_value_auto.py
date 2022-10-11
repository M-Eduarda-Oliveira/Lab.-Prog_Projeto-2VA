from data.registration_car import registrationsCar
from utils.format_BRL import formatBRL

def updateValueAuto():
  chassi = input("Digite o chassi do Automóvel: ")
  novoValor = float(input("Digite o Novo Valor do Automóvel: "))
  registrationsCar[chassi][3] = novoValor
  print(f'O Novo Valor foi Cadastrado: R$ {formatBRL(registrationsCar[chassi][3])}')
