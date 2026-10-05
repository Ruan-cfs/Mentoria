# ==========================================
# PROJETO DE MONITORIA: SISTEMA DE NOTAS
# Conteúdos: Condicionais, Strings e Funções
# ==========================================

# 1. FUNÇÕES DE MANIPULAÇÃO DE STRINGS
def limpar_nome(nome):
    # strip() remove espaços das pontas | title() deixa a primeira letra maiúscula
    nome_limpo = nome.strip().title()
    return nome_limpo


# 2. FUNÇÕES COM CONDICIONAIS
def verificar_situacao(nota):
    if nota >= 7.0:
        return "APROVADO(A)"
    elif nota >= 5.0:
        return "EM RECUPERAÇÃO"
    else:
        return "REPROVADO(A)"


# 3. FUNÇÃO PRINCIPAL QUE JUNTA TUDO
def processar_aluno(nome_digitação, nota_aluno):
    nome_correto = limpar_nome(nome_digitação)
    resultado = verificar_situacao(nota_aluno)
    
    print("---------------------------------")
    print("Aluno:", nome_correto)
    print("Nota final:", nota_aluno)
    print("Situação:", resultado)
    print("---------------------------------")


# ==========================================
# TESTANDO O PROGRAMA
# ==========================================

# Exemplo 1: Nome com letras desordenadas e espaços
processar_aluno("   maria EDUARDA  ", 8.5)

# Exemplo 2: Aluno em recuperação
processar_aluno("LUCAS silva", 5.5)

# Exemplo 3: Aluno reprovado
processar_aluno("  pedro   ", 3.0)