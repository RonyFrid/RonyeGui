def define_posicoes(linha, coluna, orientacao, tamanho):
    posicoes = []

    for i in range(tamanho):
        if orientacao == "vertical":
            posicoes.append([linha + i, coluna])
        else:  
            posicoes.append([linha, coluna + i])

    return posicoes




def afundados(frota, tabuleiro):
    quantidade = 0

    for embarcacoes in frota.values():
        for navio in embarcacoes:
            afundado = True

            for linha, coluna in navio:
                if tabuleiro[linha][coluna] != 'X':
                    afundado = False
                    break

            if afundado:
                quantidade += 1

    return quantidade


def posicao_valida(frota, linha, coluna, orientacao, tamanho):
    posicoes = define_posicoes(linha, coluna, orientacao, tamanho)

    for linha_navio, coluna_navio in posicoes:
        if linha_navio < 0 or linha_navio >= 10:
            return False
        if coluna_navio < 0 or coluna_navio >= 10:
            return False

        for embarcacoes in frota.values():
            for navio in embarcacoes:
                for linha_ocupada, coluna_ocupada in navio:
                    if [linha_navio, coluna_navio] == [linha_ocupada, coluna_ocupada]:
                        return False

    return True


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
    print(f"Insira as informações referentes ao navio {nome_navio} que possui tamanho {tamanho}")

    for i in range(quantidade):
        while True:
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
        frota = preenche_frota(
            frota, nome_navio, linha, coluna, orientacao, tamanho
        )

print(frota)