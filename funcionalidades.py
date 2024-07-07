from datetime import datetime, timedelta

# Função para calcular a data de devolução com base na data atual e no prazo em dias
def calcular_data_devolucao(prazo_dias):
    data_atual = datetime.now()
    prazo = timedelta(days=prazo_dias)
    data_devolucao = data_atual + prazo
    return data_devolucao

# Exemplo de uso da função para calcular a data de devolução com prazo de 7 dias
prazo_devolucao = int(input('Por quanto tempo você deseja alugar o veículo(a partir da data atual)? '))
data_devolucao = calcular_data_devolucao(prazo_devolucao)

print("Data atual:", datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
print(f"Prazo de devolução: {prazo_devolucao} dias")
print("Data de devolução esperada:", data_devolucao.strftime("%Y-%m-%d %H:%M:%S"))
