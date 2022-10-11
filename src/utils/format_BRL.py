# Função para formatar saída em valor monetário (R$)
def formatBRL(value):
  a = "{:,.2f}".format(float(value))
  b = a.replace(',', 'v')
  c = b.replace('.', ',')
  return c.replace('v', '.')