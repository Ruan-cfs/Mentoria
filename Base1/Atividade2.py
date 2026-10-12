def Avaliar_candidato(nome,nota_teste,nota_entrevista,experiencia,idade):

    if nota_teste or nota_entrevista < 0 and experiencia < 0 and idade < 16:
        mensagem = "Não poderá participar da entrevista"

