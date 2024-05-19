import numpy as np
import matplotlib.pyplot as plt

N = 10000
I = 1
S = N - I
R = 0
beta = 0.3
gamma = 0.05

susceptible = [S]
infected = [I]
recovered = [R]

for _ in range(1000):
    # count the prabability at each point
    prob_infection = beta * (I / N)
    prob_recovery = gamma
    
    # count the number of people
    newly_infected = np.random.choice([0, 1], S, p=[1 - prob_infection, prob_infection]).sum()
    newly_recovered = np.random.choice([0, 1], I, p=[1 - prob_recovery, prob_recovery]).sum()
    
    S -= newly_infected
    I += newly_infected - newly_recovered
    R += newly_recovered
    
    susceptible.append(S)
    infected.append(I)
    recovered.append(R)

plt.figure(figsize=(6, 4), dpi=150)
plt.plot(susceptible, label='Susceptible')
plt.plot(infected, label='Infected')
plt.plot(recovered, label='Recovered')
plt.xlabel('Time')
plt.ylabel('Population')
plt.title('SIR Model')
plt.legend()

save_path = "/Users/madongge/Downloads/IBI1/IBI1_2023-24/Practical10/SIR_Model_Plot.png"
plt.savefig(save_path)
plt.show()
