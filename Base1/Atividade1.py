#estatística de 3 cidades:

def Dados_cidade(numero_habitantes,numero_nascido):
    
    taxa_natalidade = (numero_nascido * 1000)/numero_habitantes
    return taxa_natalidade , numero_nascido


cidade1, num_nac1 = Dados_cidade(32000,150)
cidade2, num_nac2 = Dados_cidade(55000,324)
cidade3, num_nac3 = Dados_cidade(125689,13)

def verificar_taxa(taxa1=cidade1,taxa2=cidade2,taxa3=cidade3,
    num_nac1=num_nac1,num_nac2=num_nac2,num_nac3=num_nac3):

    if taxa1 < taxa2 or (taxa1 == taxa2 and num_nac1 < num_nac2):
        taxa1, taxa2 = taxa2, taxa1
        num_nac1, num_nac2 = num_nac2, num_nac1

    if taxa1 < taxa3 or (taxa1 == taxa3 and num_nac1 < num_nac3):
        taxa1, taxa3 = taxa3, taxa1
        num_nac1, num_nac3 = num_nac3, num_nac1

    if taxa2 < taxa3 or (taxa2 == taxa3 and num_nac2 < num_nac3):
        taxa2, taxa3 = taxa3, taxa2
        num_nac2, num_nac3 = num_nac3, num_nac2

    return taxa1 , taxa3

def media_cidade(cidade1=num_nac1,cidade2=num_nac2,cidade3=num_nac3):

    media = (cidade1 + cidade2 + cidade3)/ 3

    return media

maior_taxa, menor_taxa = verificar_taxa()

print("Em uma pesquisa feita em três cidades diferentes obteve-se:")
print(f"A maior taxa de natalidade é de {maior_taxa:.2f} e a menor {menor_taxa:.2f}")
print(f"com uma média de nascidos {media_cidade():.2f} nas três cidades.")
