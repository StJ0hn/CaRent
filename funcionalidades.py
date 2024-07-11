from datetime import datetime, timedelta


print('''\033[1;33m
    <=><=><=><=><=><=>\033[m
    |    \033[1;32mCar.Rent\033[m    |
    \033[1;33m<=><=><=><=><=><=>\033[m
    Modelos e tabela de preços:
    1 - Renault "Duster" (R$ 23,00 p/dia)
    2 - Fiat "Uno" (R$ 15,00 p/dia)
    3 - Chevrollet "Silverado" (R$ 20,00 p/dia)''')
print('<=>' * 15)
opção = int(input('\033[1;32mQual carro você deseja escolher? \033[m'))
print('<=>' * 15)


# Função para calcular a data de devolução e calcular custo:
def ddevo_e_custo(prazo_dias=None):
    if prazo_dias == None:
        prazo_devolucao = int(input('Por quanto dias você deseja alugar o carro (a partir de hoje)? '))
        print()
        prazo_dias
        prazo_dias = prazo_devolucao
        data_atual = datetime.now()
        prazo = timedelta(days=prazo_dias)
        data_devolucao = data_atual + prazo
    if opção == 1:
        custo = prazo_dias * 23
        print(f'\033[1;31mCalculando o tempo de aluguel...O valor será:\033[m R${custo:.2f}')
        print()
    if opção == 2:
        custo = prazo_dias * 15
        print(f'\033[1;31mCalculando o tempo de aluguel...O valor será:\033[m R${custo:.2f}')
        print()
    if opção == 3:
        custo = prazo_dias * 20
        print(f'\033[1;31mCalculando o tempo de aluguel...O valor será:\033[m R${custo:.2f}')
        print()
    # Exemplo de uso da função para calcular a data de devolução e os custos:
    print("\033[1;34mData atual:\033[m", datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
    print('\033[33m<=>\033[m' * 15)
    print(f"\033[1;34mPrazo de devolução:\033[m {prazo_devolucao} dias")
    print('\033[33m<=>\033[m' * 15)
    print("\033[1;34mData de devolução esperada:\033[m", data_devolucao.strftime("%Y-%m-%d %H:%M:%S"))
    print('\033[33m<=>\033[m' * 15)
    #Calculando custos com base no prazo: