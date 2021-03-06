import csv
import matplotlib.pyplot as plt

# Vamos ler os dados como uma lista
print("Lendo o documento...")
with open("chicago.csv", "r") as file_read:
    reader = csv.reader(file_read)
    data_list = list(reader)
print("Ok!")

# Vamos verificar quantas linhas nós temos
print("Número de linhas:")
print(len(data_list))

# Imprimindo a primeira linha de data_list para verificar se funcionou.
print("Linha 0: ")
print(data_list[0])
# É o cabeçalho dos dados, para que possamos identificar as colunas.

# Imprimindo a segunda linha de data_list, ela deveria conter alguns dados
print("Linha 1: ")
print(data_list[1])

input("Aperte Enter para continuar...")
# TAREFA 1
# TODO: Imprima as primeiras 20 linhas usando um loop para identificar os dados.
print("\n\nTAREFA 1: Imprimindo as primeiras 20 amostras")

for i, row in enumerate(data_list):
    print("Linha {}:". format(i))
    print(row)
    if i >= 21:
            print("\nA primeira tarefa termina aqui!")
            break
"""
enumerate()
    Iterar os valores de uma lista junto com o index.
    Os indices são criados quando se obtém um objeto de intervalo do zero até a extensão da lsita menos 1.
"""

# Vamos mudar o data_list para remover o cabeçalho dele.
data_list = data_list[1:]

# Nós podemos acessar as features pelo índice
# Por exemplo: sample[6] para imprimir gênero, ou sample[-2]

input("Aperte Enter para continuar...")
# TAREFA 2
# TODO: Imprima o `gênero` das primeiras 20 linhas

print("\nTAREFA 2: Imprimindo o gênero das primeiras 20 amostras")

for i, row in enumerate(data_list):
    print("Gênero Usuário {}:".format(i));
    print(row[6]);
    if i >= 20:
        print("\nA segunda tarefa termina aqui!")
        break

# Ótimo! Nós podemos pegar as linhas(samples) iterando com um for, e as colunas(features) por índices.
# Mas ainda é difícil pegar uma coluna em uma lista. Exemplo: Lista com todos os gêneros

input("Aperte Enter para continuar...")
# TAREFA 3
# TODO: Crie uma função para adicionar as colunas(features) de uma lista em outra lista, na mesma ordem
def column_to_list(data, i):
    column_list = []
    """
    Adicionando as colunas de uma lista - data_list - em outra lista, na mesma ordem.
    INPUT:
    data: list. O dataset do projeto.
    i: int. O índice que ajudará a transformar em column.
    OUTPUT:
    column_to_list: column_list. A coluna selecionada através índice em forma de lista.
    """
    # Dica: Você pode usar um for para iterar sobre as amostras, pegar a feature pelo seu índice, e dar append para uma lista
    for row in data:
        column = row[i]
        column_list.append(column)
    return column_list

# Vamos checar com os gêneros se isso está funcionando (apenas para os primeiros 20)
print("\nTAREFA 3: Imprimindo a lista de gêneros das primeiras 20 amostras")
print(column_to_list(data_list, -2)[:20])
print("\nA terceira tarefa termina aqui!")
# ------------ NÃO MUDE NENHUM CÓDIGO AQUI ------------
assert type(column_to_list(data_list, -2)) is list, "TAREFA 3: Tipo incorreto retornado. Deveria ser uma lista."
assert len(column_to_list(data_list, -2)) == 1551505, "TAREFA 3: Tamanho incorreto retornado."
assert column_to_list(data_list, -2)[0] == "" and column_to_list(data_list, -2)[1] == "Male", "TAREFA 3: A lista não coincide."
# -----------------------------------------------------

input("Aperte Enter para continuar...")
# Agora sabemos como acessar as features, vamos contar quantos Male (Masculinos) e Female (Femininos) o dataset tem
# TAREFA 4
# TODO: Conte cada gênero. Você não deveria usar uma função parTODO isso.
male = 0
female = 0


# Verificando o resultado
print("\nTAREFA 4: Imprimindo quantos masculinos e femininos nós encontramos")

male = int(column_to_list(data_list, -2).count("Male"))
female = int(column_to_list(data_list, -2).count("Female"))

print("Número de Mulheres: {}".format(female))
print("Número de Homens: {}".format(male))
print("\nA quarta tarefa termina aqui!")


# ------------ NÃO MUDE NENHUM CÓDIGO AQUI ------------
assert male == 935854 and female == 298784, "TAREFA 4: A conta não bate."
# -----------------------------------------------------

input("Aperte Enter para continuar...")
# Por que nós não criamos uma função parTODO isso?
# TAREFA 5
# TODO: Crie uma função para contar os gêneros. Retorne uma lista.
# Isso deveria retornar uma lista com [count_male, count_female] (exemplo: [10, 15] significa 10 Masculinos, 15 Femininos)
column_gender = column_to_list(data_list, -2)

def count_gender(data_list):    
    """
        Contando o número de pessoas de cada gênero.
        INPUT:
        data_list: List. O dataset completo.
        OUTPUT:
        count_gender: [male, female].. O número de homens e mulheres, em forma de lista.
    """
    male = 0
    female = 0
    for gender in column_gender:
        if gender == "Female":
            female += 1
        if gender == "Male":
            male += 1
    return [male, female]

print("\nTAREFA 5: Imprimindo o resultado de count_gender")
print(count_gender(data_list))
print("\nA quinta tarefa termina aqui!")

# ------------ NÃO MUDE NENHUM CÓDIGO AQUI ------------
assert type(count_gender(data_list)) is list, "TAREFA 5: Tipo incorreto retornado. Deveria retornar uma lista."
assert len(count_gender(data_list)) == 2, "TAREFA 5: Tamanho incorreto retornado."
assert count_gender(data_list)[0] == 935854 and count_gender(data_list)[1] == 298784, "TAREFA 5: Resultado incorreto no retorno!"
# -----------------------------------------------------

input("Aperte Enter para continuar...")
# Agora que nós podemos contar os usuários, qual gênero é mais prevalente?
# TAREFA 6
# TODO: Crie uma função que pegue o gênero mais popular, e retorne este gênero como uma string.
# Esperamos ver "Masculino", "Feminino", ou "Igual" como resposta.
def most_popular_gender(data_list):
    """
        Calcular o gênero mais poupular.
        INPUT:
        data_list: List. O dataset completo.
        OUTPUT:
        most_popular_gender: answer. Str. A resposta do gênero mais popular, em forma de string.
    """
    answer = ""
    if male > female:
        answer = "Masculino"
    elif female < male:
        answer = "Feminino"
    else:
        answer = "Igual"
    return answer

print("\nTAREFA 6: Qual é o gênero mais popular na lista?")
print("O gênero mais popular na lista é: ", most_popular_gender(data_list))
print("\nA sexta tarefa termina aqui!")

# ------------ NÃO MUDE NENHUM CÓDIGO AQUI ------------
assert type(most_popular_gender(data_list)) is str, "TAREFA 6: Tipo incorreto no retorno. Deveria retornar uma string."
assert most_popular_gender(data_list) == "Masculino", "TAREFA 6: Resultado de retorno incorreto!"
# -----------------------------------------------------

# Se tudo está rodando como esperado, verifique este gráfico!
gender_list = column_to_list(data_list, -2)
types = ["Male", "Female"]
quantity = count_gender(data_list)
y_pos = list(range(len(types)))
plt.bar(y_pos, quantity)
plt.ylabel('Quantidade')
plt.xlabel('Gênero')
plt.xticks(y_pos, types)
plt.title('Quantidade por Gênero')
plt.show(block=True)

input("Aperte Enter para continuar...")
# TAREFA 7
# TODO: Crie um gráfico similar para user_types. Tenha certeza que a legenda está correta.
print("\nTAREFA 7: Verifique o gráfico!")

user_type = column_to_list(data_list, 5) # A coluna do tipo do usuário

def count_user_type(data_list):
    """
    Contar o número de usuários que são subscribers e contar o número de customers.
    INPUT:
    data_list: List. O dataset em forma de lista.
    OUTPUT:
    count_user_type: [subscriber, customer]. O número de usuários subscribers e customers em lista.
    """
    subcriber = 0
    customer = 0
    for user in user_type:
        if user == "Subscriber":
            subcriber += 1
        if user == "Customer":
            customer += 1
    return [subcriber, customer]

user_type = column_to_list(data_list, 5) #Temos a coluna de usuários
types = ["Subscriber", "Customer"]
quantity = count_user_type(data_list)
y_pos = list(range(len(types)))
plt.bar(y_pos, quantity)
plt.ylabel('Quantidade')
plt.xlabel('User Type')
plt.xticks(y_pos, types)
plt.title('Quantidade por User Type')
plt.show(block=True)

print("\nA sétima tarefa termina aqui!")

input("Aperte Enter para continuar...")
# TAREFA 8
# TODO: Responda a seguinte questão
male, female = count_gender(data_list)
print("\nTAREFA 8: Por que a condição a seguir é Falsa?")
print("male + female == len(data_list):", male + female == len(data_list))
answer = "Porque a função len() retorna o número de itens em um objeto. E o número total de objetos na coluna de gênero não é apenas male + female, já que existem espaços em branco."
print("resposta:", answer)

print("\nA oitava tarefa termina aqui!")

# ------------ NÃO MUDE NENHUM CÓDIGO AQUI ------------
assert answer != "Escreva sua resposta aqui.", "TAREFA 8: Escreva sua própria resposta!"
# -----------------------------------------------------

input("Aperte Enter para continuar...")
# Vamos trabalhar com trip_duration (duração da viagem) agora. Não conseguimos tirar alguns valores dele.
# TAREFA 9
# TODO: Ache a duração de viagem Mínima, Máxima, Média, e Mediana.
# Você não deve usar funções prontas parTODO isso, como max() e min().
trip_duration_list = column_to_list(data_list, 2)
min_trip = 0.
max_trip = 0.
mean_trip = 0.
median_trip = 0.


print("\nTAREFA 9: Imprimindo o mínimo, máximo, média, e mediana")
trip_duration_list = [float(i) for i in trip_duration_list]
trip_duration_list.sort()

max_trip = trip_duration_list[0]
for n in trip_duration_list:
    if max_trip < n:
        max_trip = n
print("\nValor máximo: {}".format(int(max_trip)))

min_trip = trip_duration_list[0]
for n in trip_duration_list:
    if min_trip > n:
        min_trip = n
print("\nValor mínimo: {}".format(int(min_trip)))

mean_trip = 0
for n in trip_duration_list:
    mean_trip = mean_trip + n
mean_trip = round(mean_trip/len(trip_duration_list))
print("\nMédia: {}".format(mean_trip))

median_trip = 0
duration_ordenada = sorted(trip_duration_list)
qtde_n_duration = len(trip_duration_list)
center_duration = len(trip_duration_list)/2

for n in trip_duration_list:
    if len(duration_ordenada) % 2 != 0: #ÍMPAR
        median_trip = trip_duration_list[len(trip_duration_list) // 2]
    if len(duration_ordenada) % 2 == 0:
        temp = 0.0
        median_parties = []
        median_parties = duration_ordenada[center_duration - 1 : center_duration + 1]
        for n in median_parties:
            temp += value
            median_trip = temp / 2
print("Mediana: {}".format(int(median_trip)))


mean_trip = round(sum(trip_duration_list)/len(trip_duration_list))
median_trip = round(trip_duration_list[len(trip_duration_list)//2])

print("Min: ", min_trip, "Max: ", max_trip, "Média: ", mean_trip, "Mediana: ", median_trip)

print("\nA nona tarefa termina aqui!")

# ------------ NÃO MUDE NENHUM CÓDIGO AQUI ------------
assert round(min_trip) == 60, "TAREFA 9: min_trip com resultado errado!"
assert round(max_trip) == 86338, "TAREFA 9: max_trip com resultado errado!"
assert round(mean_trip) == 940, "TAREFA 9: mean_trip com resultado errado!"
assert round(median_trip) == 670, "TAREFA 9: median_trip com resultado errado!"
# -----------------------------------------------------

input("Aperte Enter para continuar...")
# TAREFA 10
# Gênero é fácil porque nós temos apenas algumas opções. E quanto a start_stations? Quantas opções ele tem?
# TODO: Verifique quantos tipos de start_stations nós temos, usando set()
start_stations = set(column_to_list(data_list, 3))

print("\nTAREFA 10: Imprimindo as start stations:")
print("Quantidade de start stations: {}".format(len(start_stations)))
print(start_stations)

# ------------ NÃO MUDE NENHUM CÓDIGO AQUI ------------
assert len(start_stations) == 582, "TAREFA 10: Comprimento errado de start stations."
# -----------------------------------------------------
