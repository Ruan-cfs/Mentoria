def Avaliar_candidato(nota_teste,nota_entrevista,experiencia,idade):

    if (nota_teste < 0 or nota_teste > 100 or nota_entrevista < 0 or nota_entrevista > 100) and (experiencia <= 0) and (idade < 16):
        mensagem = "Dados invalidos"
    elif nota_teste < 40 or nota_entrevista < 50:
        mensagem = "Reprovacao direta"
    elif nota_teste >= 80 and nota_entrevista >= 70 and experiencia > 6:
        mensagem = "Aprovado direto"
    elif (nota_entrevista + nota_teste) >= 130 and nota_entrevista > 60:
        mensagem = "Segunda etapa"
    else:
        mensagem = "Banco de talentos"

    return mensagem


def classificar_candidato(not_teste,nota_entrevista,experi,idade):

    mensagem = Avaliar_candidato(not_teste,nota_entrevista,experi,idade)

    if mensagem == "Dados invalidos":
        return -1
    elif mensagem == "Reprovacao direta":
        return 0
    elif mensagem == "Aprovado direto":
        return 3
    elif mensagem == "Segunda etapa":
        return 2
    else:
        return 1

    

def main():
    not_teste,nota_entrevista,experi,idade = map( int, input().split())
    
    print(Avaliar_candidato(not_teste,nota_entrevista,experi,idade))
    print(classificar_candidato(not_teste,nota_entrevista,experi,idade))

main()

     


