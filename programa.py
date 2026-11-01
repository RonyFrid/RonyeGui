from funcoes import define_posicoes, posicao_valida, preenche_frota

frota = {
    "porta-aviões": [],
    "navio-tanque": [],
    "contratorpedeiro": [],
    "submarino": []
}

navios = [
    ("porta-aviões", 4, 1),
    ("navio-tanque", 3, 2),
    ("contratorpedeiro", 2, 3),
    ("submarino", 1, 4)
]

for nome_navio, tamanho, quantidade in navios:
    for i in range(quantidade):
        while True:
            print(
                f"Insira as informações referentes ao navio {nome_navio} "
                f"que possui tamanho {tamanho}"
            )

            linha = int(input())
            coluna = int(input())

            if nome_navio == "submarino":
                orientacao = "vertical"
            else:
                escolha_orientacao = int(input())

                if escolha_orientacao == 1:
                    orientacao = "vertical"
                else:
                    orientacao = "horizontal"

            if posicao_valida(frota, linha, coluna, orientacao, tamanho):
                break

            print("Esta posição não está válida!")

        posicoes = define_posicoes(linha, coluna, orientacao, tamanho)
        frota = preenche_frota(frota, nome_navio, linha, coluna, orientacao, tamanho)

print(frota)
        