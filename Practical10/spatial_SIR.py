import numpy as np
import matplotlib.pyplot as plt

beta = 0.3
gamma = 0.05
#100x100 array
population = np.zeros((100, 100))

outbreak = np.random.choice(range(100), 2)
population[outbreak[0], outbreak[1]] = 1  

for t in range(100):
    new_population = population.copy()
    
    for i in range(100):
        for j in range(100):
            if population[i, j] == 1:  
                neighbors = [(i-1, j-1), (i-1, j), (i-1, j+1),
                             (i, j-1),             (i, j+1),
                             (i+1, j-1), (i+1, j), (i+1, j+1)]
                for ni, nj in neighbors:
                    if 0 <= ni < 100 and 0 <= nj < 100:  
                        if population[ni, nj] == 0:  
                            if np.random.random() < beta:
                                new_population[ni, nj] = 1  
                if np.random.random() < gamma:
                    new_population[i, j] = 2  

    population = new_population

    plt.figure(figsize=(6, 4), dpi=150)
    plt.imshow(population, cmap='viridis', interpolation='nearest')
    plt.title(f'Time Point: {t}')
    plt.show()
