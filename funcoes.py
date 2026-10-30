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