from datetime import datetime, timedelta

def printar_verde(texto):
    print(f'\033[1;32m{texto}\033[m', end="")

def printar_vermelho(texto):
    print(f'\033[1;31m{texto}\033[m', end="")

def printar_azul(texto):
    print(f'\033[1;34m{texto}\033[m', end="")

def mostrar_menu():
    print('''\033[1;33m
    <=><=><=><=><=><=>\033[m
    |    \033[1;32mCar.Rent\033[m    |
    \033[1;33m<=><=><=><=><=><=>\033[m
    Modelos e tabela de preços:
    1 - Renault "Duster" (R$ 23,00 p/dia)
    2 - Fiat "Uno" (R$ 15,00 p/dia)
    3 - Chevrollet "Silverado" (R$ 20,00 p/dia)''')

def mostrar_decoracao():
    print('<=>' * 15)

def pegar_modelo_de_carro():
    
    selecionou_modelo_valido = False

    while not selecionou_modelo_valido:
        try:
            mostrar_decoracao()
            opção = int(input('\033[1;32mQual carro você deseja escolher? \033[m'))
            mostrar_decoracao()
            if opção > 0 and opção < 4:
                return opção
            else:
                printar_vermelho("ERRO: ")
                print("selecione um valor entre 1 e 3")
        except:
            printar_vermelho("ERRO: ")
            print('Insira uma opção válida.')

def pegar_dias_de_aluguel():
    while True:
        try:
            prazo_devolucao = int(input('Por quanto dias você deseja alugar o carro (a partir de hoje)? '))
            if prazo_devolucao > 365 or prazo_devolucao < 1:
                printar_vermelho("ERRO: ")
                print("selecione um valor entre 1 e 365 dias.")
                continue
            return prazo_devolucao
        except:
            printar_vermelho("ERRO: ")
            print("tente novamente.\n")

def calcular_data_de_devolucao(data_de_aluguel):
    prazo_dias = data_de_aluguel
    data_atual = datetime.now()
    prazo = timedelta(days=prazo_dias)
    data_devolucao = data_atual + prazo
    return data_devolucao

# Função para calcular a data de devolução e calcular custo:
def ddevo_e_custo(prazo_dias=None):

    mostrar_menu()
    modelo = pegar_modelo_de_carro()
    dias_de_aluguel = pegar_dias_de_aluguel()
    data_de_devolucao = calcular_data_de_devolucao(dias_de_aluguel)

    if modelo == 1:
        custo = dias_de_aluguel * 23
        printar_vermelho("Calculando o tempo de aluguel...O valor será:")
        print(f'{custo:.2f}\n')
    if modelo == 2:
        custo = dias_de_aluguel * 15
        printar_vermelho("Calculando o tempo de aluguel...O valor será:")
        print(f'{custo:.2f}\n')
    if modelo == 3:
        custo = dias_de_aluguel * 20
        printar_vermelho("Calculando o tempo de aluguel...O valor será:")
        print(f'{custo:.2f}\n')
    
    # Exemplo de uso da função para calcular a data de devolução e os custos:
    print("\033[1;34mData atual:\033[m", datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
    print('\033[33m<=>\033[m' * 15)
    print(f"\033[1;34mPrazo de devolução:\033[m {dias_de_aluguel} dias")
    print('\033[33m<=>\033[m' * 15)
    print("\033[1;34mData de devolução esperada:\033[m", data_de_devolucao.strftime("%Y-%m-%d %H:%M:%S"))
    print('\033[33m<=>\033[m' * 15)