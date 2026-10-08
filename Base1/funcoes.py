'''
    1. O que é uma Função?
Pense em uma função como uma máquina de suco:
Parâmetros (Entradas): São as frutas que você coloca na máquina (ex: laranja, açúcar).
O Corpo da Função: É a lâmina da máquina que processa as frutas.
O return (Saída): É o copo de suco pronto que a máquina devolve para você.
Sem a máquina, toda vez que você quisesse suco, teria que cortar e espremer as frutas na mão, 
repetindo todos os passos. Com a máquina pronta, você só precisa ligá-la e trocar as frutas!'''

def maquina_suco(fruta):

    suco = f"Suco natural de {fruta}"

    return suco

copo1 = maquina_suco("Laranja")
copo2 = maquina_suco("Maracujá")

print(copo1)