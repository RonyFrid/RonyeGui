from funcoes import define_posicoes, posicao_valida, preenche_frota, posiciona_frota, faz_jogada, afundados


def monta_tabuleiros(tabuleiro_jogador, tabuleiro_oponente):
    texto = ''
    texto += '   0  1  2  3  4  5  6  7  8  9         0  1  2  3  4  5  6  7  8  9\n'
    texto += '_______________________________      _______________________________\n'
    for linha in range(len(tabuleiro_jogador)):
        jogador_info = '  '.join([str(item) for item in tabuleiro_jogador[linha]])
        oponente_info = '  '.join([
            info if str(info) in 'X-' else '0'
            for info in tabuleiro_oponente[linha]
        ])
        texto += f'{linha}| {jogador_info}|     {linha}| {oponente_info}|\n'

    return texto


frota = {
    'porta-aviões': [],
    'navio-tanque': [],
    'contratorpedeiro': [],
    'submarino': []
}

navios = [
    ('porta-aviões', 4, 1),
    ('navio-tanque', 3, 2),
    ('contratorpedeiro', 2, 3),
    ('submarino', 1, 4)
]

for nome_navio, tamanho, quantidade in navios:
    for i in range(quantidade):
        while True:
            print(f'Insira as informações referentes ao navio {nome_navio} que possui tamanho {tamanho}')

            linha = int(input('Linha: '))
            coluna = int(input('Coluna: '))

            if nome_navio == 'submarino':
                orientacao = 'vertical'
            else:
                escolha_orientacao = int(input('Orientação: [1] Vertical [2] Horizontal '))

                if escolha_orientacao == 1:
                    orientacao = 'vertical'
                else:
                    orientacao = 'horizontal'

            if posicao_valida(frota, linha, coluna, orientacao, tamanho):
                break

            print('Esta posição não está válida!')

        posicoes = define_posicoes(linha, coluna, orientacao, tamanho)
        frota = preenche_frota(frota, nome_navio, linha, coluna, orientacao, tamanho)


frota_oponente = {
    'porta-aviões': [
        [[9, 1], [9, 2], [9, 3], [9, 4]]
    ],
    'navio-tanque': [
        [[6, 0], [6, 1], [6, 2]],
        [[4, 3], [5, 3], [6, 3]]
    ],
    'contratorpedeiro': [
        [[1, 6], [1, 7]],
        [[0, 5], [1, 5]],
        [[3, 6], [3, 7]]
    ],
    'submarino': [
        [[2, 7]],
        [[0, 6]],
        [[9, 7]],
        [[7, 6]]
    ]
}

tabuleiro_jogador = posiciona_frota(frota)
tabuleiro_oponente = posiciona_frota(frota_oponente)

posicoes_informadas = []
jogando = True

total_navios = 0

for embarcacoes in frota_oponente.values():
    total_navios += len(embarcacoes)

while jogando:
    print(monta_tabuleiros(tabuleiro_jogador, tabuleiro_oponente))

    while True:
        while True:
            linha = int(input('Jogador, qual linha deseja atacar? '))

            if 0 <= linha <= 9:
                break

            print('Linha inválida!')

        while True:
            coluna = int(input('Jogador, qual coluna deseja atacar? '))

            if 0 <= coluna <= 9:
                break

            print('Coluna inválida!')

        if [linha, coluna] in posicoes_informadas:
            print(f'A posição linha {linha} e coluna {coluna} já foi informada anteriormente!')
        else:
            break

    posicoes_informadas.append([linha, coluna])

    tabuleiro_oponente = faz_jogada(tabuleiro_oponente, linha, coluna)

    if afundados(frota_oponente, tabuleiro_oponente) == total_navios:
        print('Parabéns! Você derrubou todos os navios do seu oponente!')
        jogando = False

