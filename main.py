import numpy as np
import random
data = np.loadtxt('cidades.mat')

print(data)

def cvfun(pop, x, y):
    """
    Calculate the total distance for each route in the population.

    Parameters:
        pop (np.ndarray): 2D array where each row is a route through cities.
        x (np.ndarray): 1D array of x-coordinates of the cities.
        y (np.ndarray): 1D array of y-coordinates of the cities.

    Returns:
        np.ndarray: Array of distances for each route in `pop`.
    """
    Npop, Ncidade = pop.shape
    # Add the first city at the end of each route to complete the tour
    tour = np.hstack((pop, pop[:, [0]]))

    # Calculate distance matrix for all city pairs
    dcidade = np.zeros((Ncidade, Ncidade))
    for i in range(Ncidade):
        for j in range(Ncidade):
            dcidade[i, j] = np.sqrt((x[i] - x[j])**2 + (y[i] - y[j])**2)

    # Calculate total distance for each tour in the population
    dist = np.zeros((Npop, 1))
    for i in range(Npop):
        for j in range(Ncidade):
            dist[i, 0] += dcidade[tour[i, j], tour[i, j + 1]]

    return dist

population = []
for i in range(0, 20):
    array = random.sample(range(1, 21), 20)
    population.append(array)


pop = np.array(population)
print(pop)
print(pop.shape)

x_values = []
for i in range(0, 20):

    x_values.append(data[0][pop[]])

