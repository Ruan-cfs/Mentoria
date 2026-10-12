def Avaliar_candidato(nota_teste,nota_entrevista,experiencia,idade):

    if nota_teste or nota_entrevista < 0 and experiencia < 0 and idade < 16:
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


def classificar_candidato():
    not_teste,nota_entrevista,experi,idade = map( int, input().split())

    if Avaliar_candidato(not_teste,nota_entrevista,experi,idade) == "Dados invalidos":
        return -1
    elif Avaliar_candidato(not_teste,nota_entrevista,experi,idade) == "Reprovacao direta":
        return 0
    elif Avaliar_candidato(not_teste,nota_entrevista,experi,idade) == "Aprovado direto":
        return 1
    elif Avaliar_candidato(not_teste,nota_entrevista,experi,idade) == "Segunda etapa":
        return 2
    else:
        return 3

def main():
    
    print(classificar_candidato())

main()

     


