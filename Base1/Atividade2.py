def Avaliar_candidato(nome,nota_teste,nota_entrevista,experiencia,idade):

    if nota_teste or nota_entrevista < 0 and experiencia < 0 and idade < 16:
        print(f"O candidato {nome} Não poderá participar da entrevista")
    elif nota_teste < 40 or nota_entrevista < 50:
        print(f"Candidato {nome} Reprovado")
    elif nota_teste >= 80 and nota_entrevista >= 70 and experiencia > 6:
        print(f"Candidato {nome} Aprovado na primeira etapa")
    elif (nota_entrevista + nota_teste) >= 130 and nota_entrevista > 60:
        print(f"Candidato {nome} Aprovado na segunda etapa")
    else:
        print(f"Candidato {nome} no banco de talentos")

nome,not_teste,nota_entrevista,experi,idade = input().split()
not_teste,nota_entrevista,experi,idade = int(not_teste) , int(nota_entrevista), int(experi), int(idade)

Avaliar_candidato(nome,not_teste,nota_entrevista,experi,idade)




