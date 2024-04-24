#

import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm

N = 10000
I = 1
S = N - I
R = 0
beta = 0.3
gamma = 0.05

# 不同接种率下的模拟
vaccination_rates = np.linspace(0, 1, 11)  # 从 0% 到 100% 的接种率，共 11 个点

# 设置颜色
colors = cm.viridis(np.linspace(0, 1, len(vaccination_rates)))

for v_rate, color in zip(vaccination_rates, colors):
    V = int(N * v_rate)  
    susceptible = [S]
    infected = [I]
    recovered = [R]


    for _ in range(1000):
        # 计算每个时间点的概率
        prob_infection = beta * (I / N)
        prob_recovery = gamma

        # 感染者和易感染者的人数
        newly_infected = np.random.choice([0, 1], S, p=[1 - prob_infection, prob_infection]).sum()
        newly_recovered = np.random.choice([0, 1], I, p=[1 - prob_recovery, prob_recovery]).sum()

        S -= newly_infected
        I += newly_infected - newly_recovered
        R += newly_recovered

        # 记录每个时间点的结果
        susceptible.append(S)
        infected.append(I)
        recovered.append(R)

    plt.plot(infected, label=f'Vaccination Rate: {v_rate*100:.0f}%', color=color)

plt.xlabel('Time')
plt.ylabel('Number of Infected')
plt.title('SIR Model with Different Vaccination Rates')
plt.legend()
plt.show()


