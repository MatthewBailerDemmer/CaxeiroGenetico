import matplotlib.pyplot as plt
import numpy as np
import random

# Carregar os dados das cidades
data = np.loadtxt('cidades.mat')

ROLETA = []
for i in range(0, 9):
    for j in range(i):
        ROLETA.append(i)

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

    # Ordena as distâncias e mantém a correspondência com os percursos
    sorted_indices = np.argsort(dist)  # Obtém os índices das distâncias ordenadas

    # Ordena as distâncias corretamente
    dist_sorted = dist[sorted_indices]  # Ordena as distâncias em ordem crescente

    # Reorganiza a população de acordo com as distâncias ordenadas
    sorted_pop = pop[sorted_indices]  # Ordena a população com base nas distâncias

    return dist_sorted, sorted_pop


def select_parents():
    global sorted_pop, ROLETA

    random_index = random.randrange(len(ROLETA))
    random_pop_index = ROLETA[random_index]
    first_parent_r = sorted_pop[random_pop_index]

    roleta_aux = list(filter(random_pop_index.__ne__, ROLETA))

    random_index = random.randrange(len(roleta_aux))
    random_pop_index = roleta_aux[random_index]
    second_parent_r = sorted_pop[random_pop_index]

    return first_parent_r, second_parent_r


def reproduction():
    global first_parent, second_parent

    first_child = np.array(first_parent)
    second_child = np.array(second_parent)

    #Faz o primeiro swap de genes
    rand_index = random.randrange(len(first_child))
    if second_child[rand_index] == first_child[rand_index]:
        return first_child, second_child

    aux = first_child[rand_index]
    first_child[rand_index] = second_child[rand_index]
    second_child[rand_index] = aux

    #Vai retirando os genes duplicados, quando termina um automaticamente termina o outro
    condition = False
    while not condition:
        condition = True
        for zeta in range(len(first_child)):
            if first_child[zeta] == first_child[rand_index] and zeta != rand_index:
                aux = first_child[zeta]
                first_child[zeta] = second_child[zeta]
                second_child[zeta] = aux
                rand_index = zeta
                condition = False

    return first_child, second_child


def mutation(child):
    mutation_array = random.sample(range(0, 20), 2)
    #Mutation swap
    aux = child[mutation_array[0]]
    child[mutation_array[0]] = child[mutation_array[1]]
    child[mutation_array[1]] = aux

    return child


def generate_population():
    # Gerar a população de percursos (população de caminhos)
    population = []
    for m in range(20):
        array = random.sample(range(1, 21), 20)  # Números variando de 1 a 20 (representa o percurso)
        population.append(array)

    return np.array(population)


pop = generate_population()

FIRST_POPULATION = pop
POPULATION_LENGTH = pop.shape[0] * pop.shape[1]

for i in range(10000):
    # Calcular as distâncias e ordenar
    distances, sorted_pop = cvfun(pop)

    for k in range(10, 19):
        first_parent, second_parent = select_parents()
        first_descendant, second_descendant = reproduction()
        first_descendant = mutation(first_descendant)
        second_descendant = mutation(second_descendant)
        sorted_pop[k] = first_descendant
        sorted_pop[k + 1] = second_descendant

    pop = sorted_pop


x_plots = []
y_plots = []
plt.figure(figsize=(10,10), num='Caixeiro Genético').set_facecolor("black")
plt.axes().set_facecolor("black")
for i in range(20):
    x_plots.append(x[pop[0][i] - 1])
    y_plots.append(y[pop[0][i] - 1])
    plt.xlim(0, 1)
    plt.ylim(0, 1)
    plt.plot(x_plots, y_plots, linestyle="-", marker="o")
    for i in range(len(x_plots)):
        plt.text(x_plots[i], y_plots[i], str(pop[0][i]), color='white', fontsize=10)
    plt.pause(1)



print(f"Tamanho da população: {POPULATION_LENGTH}")
print(f"População inicial: \n{FIRST_POPULATION}")
print(f"População final: \n{pop}")
print(f"Número de cidades: {pop.shape[1]}")
print(f"Melhor custo: {distances[0]}")
print(f"Melhor solução: {pop[0]}")


plt.show()



