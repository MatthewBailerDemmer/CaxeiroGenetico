import numpy as np
import random

# Carregar os dados das cidades
data = np.loadtxt('cidades.mat')
print("Dados das cidades:")
print(data)

x = data[0]
y = data[1]


def cvfun(pop):
    global x, y
    Npop, Ncidade = pop.shape

    # Inicializa a matriz de distâncias entre as cidades
    dcidade = np.zeros((Ncidade, Ncidade))
    for i in range(Ncidade):
        for j in range(Ncidade):
            dcidade[i, j] = np.sqrt((x[i] - x[j]) ** 2 + (y[i] - y[j]) ** 2)

    # Inicializa o vetor de distâncias totais de cada percurso
    dist = np.zeros(Npop)

    # Calcula a distância total para cada percurso da população
    for i in range(Npop):
        for j in range(Ncidade):
            # Calcula a distância do percurso do indivíduo (tour)
            dist[i] += dcidade[pop[i, j] - 1, pop[i, (j + 1) % Ncidade] - 1]  # Ajuste para índice 0
    print(dist)
    # Ordena as distâncias e mantém a correspondência com os percursos
    sorted_indices = np.argsort(dist)  # Obtém os índices das distâncias ordenadas

    # Ordena as distâncias corretamente
    dist_sorted = dist[sorted_indices]  # Ordena as distâncias em ordem crescente

    # Reorganiza a população de acordo com as distâncias ordenadas
    sorted_pop = pop[sorted_indices]  # Ordena a população com base nas distâncias

    return dist_sorted, sorted_pop


# Gerar a população de percursos (população de caminhos)
population = []
for i in range(20):
    array = random.sample(range(1, 21), 20)  # Números variando de 1 a 20 (representa o percurso)
    population.append(array)

pop = np.array(population)
print("População original:")
print(pop)
print("Forma da população:", pop.shape)


# Calcular as distâncias e ordenar
distances, sorted_pop = cvfun(pop)
print("Distâncias ordenadas:")
print(distances)
print("População ordenada:")
print(sorted_pop)
