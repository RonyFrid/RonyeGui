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