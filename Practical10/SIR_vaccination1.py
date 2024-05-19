# 导入必要的库
import numpy as np
import matplotlib.pyplot as plt

# 定义基本变量
N = 10000
initial_vaccination_percentage = [0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
beta = 0.3
gamma = 0.05

# 初始化结果存储
results = {}

# 模拟不同的疫苗接种比例
for vac_percentage in initial_vaccination_percentage:
    vaccinated = int(N * vac_percentage / 100)
    S = 9999 - vaccinated
    I = 1
    R = vaccinated

    # 创建数组跟踪每个变量的时间变化
    S_array = [S]
    I_array = [I]
    R_array = [R]

    # 时间循环
    for t in range(1000):
        # 避免负数维度错误
        if S > 0:
            new_infected = np.random.choice(range(2), S, p=[1 - beta * I / N, beta * I / N]).sum()
        else:
            new_infected = 0

        if I > 0:
            new_recovered = np.random.choice(range(2), I, p=[1 - gamma, gamma]).sum()
        else:
            new_recovered = 0

        S = max(S - new_infected, 0)
        I = max(I + new_infected - new_recovered, 0)
        R = min(R + new_recovered, N - S - I)

        S_array.append(S)
        I_array.append(I)
        R_array.append(R)
    
    results[vac_percentage] = I_array

# 绘制结果
plt.figure(figsize=(10,6))
for vac_percentage, I_array in results.items():
    plt.plot(I_array, label=f'Vaccination {vac_percentage}%')
plt.xlabel('Time')
plt.ylabel('Number of Infected People')
plt.title('SIR Model Simulation with Vaccination')
plt.legend()
plt.show()


