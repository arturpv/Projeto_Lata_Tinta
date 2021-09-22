# Função que define a área da parede
def area():
    i = 0
    while i < 1:
        largura = float(input('Largura da parede: '))
        if 1 <= largura <= 15:
            i += 1

            j = 0
            while j < 1:
                altura = float(input('Altura da parede: '))
                if 1.1 <= altura <= 15:
                    j += 1
                else:
                    print("Insira uma altura válida!")
        else:
            print("Insira uma largura válida!")

    k = 0
    while k < 1:
        qtd_porta = int(input('Quantidade de portas: '))
        qtd_janela = int(input('Quantidade de janelas: '))

        area_janela = 2 * 1.2 * qtd_janela
        area_porta = 0.8 * 1.9 * qtd_porta
        area_parede = largura * altura
        area_portas_janelas = area_janela + area_porta

        if area_portas_janelas <= 0.5 * area_parede:
            area = area_parede - area_porta - area_janela
            k += 1

            return area
        else:
            print('Área das portas e janelas maior que 50% da área da parede.')
            print('Insira uma quantidade válida de portas e janelas.')


# Função que define a quantidade de lata de tinta que serão utilizadas.
def lata(area):
    lata_tinta = area / 5
    print(f'\nA área que será pintada é de {area:.2f}m²')
    print(f'Você irá precisar de {lata_tinta:.3f}L de tinta\n')
    lata1 = 0
    lata2 = 0
    lata3 = 0
    lata4 = 0

    if lata_tinta >= 18 and lata_tinta != 0:
        lata1 = int(lata_tinta / 18)
        lata_tinta = lata_tinta - (lata1 * 18)
    if lata_tinta >= 3.6 and lata_tinta != 0:
        lata2 = int(lata_tinta / 3.6)
        lata_tinta = lata_tinta - (lata2 * 3.6)
    if lata_tinta >= 2.5 and lata_tinta != 0:
        lata3 = int(lata_tinta / 2.5)
        lata_tinta = lata_tinta - (lata3 * 2.5)
    if lata_tinta >= 0.5 and lata_tinta != 0:
        lata4 = int(lata_tinta / 0.5)
        lata_tinta = lata_tinta - (lata4 * 0.5)
    if lata_tinta > 0:
        lata4 += 1

    if lata2 == 5:
        lata2 = 0
        lata1 += 1

    if lata4 == 5:
        lata4 = 0
        lata3 += 1

    return lata1, lata2, lata3, lata4

def main():
    i = 1
    area1 = 0
    while i < 5:
        print(f'\nInsira as medidas da {i}º parede.')
        a = area()
        area1 += a
        i += 1

    qtd = list(lata(area1))
    tam = [18, 3.6, 2.5, 0.5]

    print('Serão utilizadas: ')

    # Imprime o resultado na tela
    c = 0
    while c < 4:
        if qtd[c] > 0:
            print(f'{qtd[c]} lata(s) de {tam[c]}L')
        c += 1

# Tratativa de erro
try:
    main()
except Exception as e:
    print(f'Erro: {e}')
