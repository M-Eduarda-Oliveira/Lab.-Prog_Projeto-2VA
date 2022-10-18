from data.registration_car import registrationsCar
from utils.format_BRL import formatBRL
from utils.show_messages import showMessage

def buyInCash(chassi):
    # O valor original do produto
    valorOriginal = registrationsCar[chassi][3]
    # Desconto que será concedido
    desconto = float(input("Desconto (em %) para esse Automóvel: "))
    # Transformando a porcentagem em número decimal
    desconto = desconto / 100
    # Exibindo os Resultados
    print(f'Valor original: R$ {formatBRL(valorOriginal)}')
    print(f'Desconto ganho: R$ {formatBRL(valorOriginal * desconto)}')
    print(f'Valor com desconto: R$ {formatBRL(valorOriginal * (1-desconto))}')

def postPurchase(valueCar, valueCarInstallment, chassi, numberInstallment, rate): 
  print('============================================================')
  print(f'O Valor do Automóvel é: R$ {formatBRL(valueCar)}')
  print(f'O Valor Total do Automóvel Parcelado em {numberInstallment}x é: R$ {formatBRL(valueCarInstallment)} considerando juros de {rate}% ao mês.')
  print(f'Com Parcelas de R$ {formatBRL(valueCarInstallment / numberInstallment)} ao mês')
  confirmPurchase = input(f"Deseja Realizar a Compra em {numberInstallment}x?\nDigite 'S' para Sim, ou 'N' para Não: ").lower()

  if confirmPurchase == "s":
      registrationsCar.pop(chassi, None)
      print("Venda Realizada com Sucesso!!!")

  elif confirmPurchase == "n":
      print("Consultar Outras Condições...")
      return venderAuto()
  else:
      print("Digite uma Opção Válida!")
      return venderAuto()
  
  print('============================================================')
        
def calculateValueInstallment(method, valueCar, chassi):
  match method:
    case "1":
      calculateValueCar = valueCar * (1 + 0.05) ** 12
      postPurchase(valueCar, calculateValueCar, chassi, 12, 5)
    case "2": 
      calculateValueCar = valueCar * (1 + 0.06) ** 24
      postPurchase(valueCar, calculateValueCar, chassi, 24, 6)
    case "3":
      calculateValueCar = valueCar * (1 + 0.07) ** 36
      postPurchase(valueCar, calculateValueCar, chassi, 36, 7)
    case "4":
      calculateValueCar = valueCar * (1 + 0.08) ** 48
      postPurchase(valueCar, calculateValueCar, chassi, 48, 8)
    case _:
      showMessage(f"Digite uma opção válida.")

def venderAuto():
  chassi = input("Digite o chassi do Automóvel para Iniciar a Venda: ")

  if registrationsCar.get(chassi):
    print("Escolha a Opção de Pagamento")
    print("1 - Á Vista")
    print("2 - Parcelado")
    formaDePagamento = input("Digite o Metódo de Pagamento: ")

    if (formaDePagamento == "1"):
      buyInCash(chassi)

    elif (formaDePagamento == "2"):
      print('============================================================')
      print("Escolha a Opção de Parcelamento: ⤵")
      print("01 - 12x")
      print("02 - 24x")
      print("03 - 36x")
      print("04 - 48x")
      print('============================================================')
      valorOriginal = registrationsCar[chassi][3]
      methodOfInstallmentSelected = input("Digite a Opção Escolhida: ")
      calculateValueInstallment(methodOfInstallmentSelected, valorOriginal, chassi)
              
  else:
    showMessage('Não temos cadastro de Automóvel com este Chassi:', chassi)
