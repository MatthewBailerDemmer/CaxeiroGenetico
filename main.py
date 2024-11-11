import numpy as np
import random
data = np.loadtxt('cidades.mat')

print(data)

x = data[0]
y = data[1]
def cvfun(pop):
    global x, y
    Npop, Ncidade = pop.shape
    tour = np.hstack([pop, pop[:, :1]])
    print( tour)

    # Matriz de distâncias entre as cidades
    dcidade = np.zeros((Ncidade, Ncidade))
    for i in range(Ncidade):
        for j in range(Ncidade):
            dcidade[i, j] = np.sqrt((x[i] - x[j])**2 + (y[i] - y[j])**2)

    # Calcula a distância total para cada percurso da população
    dist = np.zeros(Npop)
    for i in range(Npop):
        for j in range(Ncidade):
            dist[i] += dcidade[tour[i, j], tour[i, j + 1]]

    return dist

population = []
for i in range(0, 20):
    array = random.sample(range(1, 21), 20)
    population.append(array)


pop = np.array(population)
print(pop)
print(pop.shape)
distances = cvfun(pop)
print(distances)



