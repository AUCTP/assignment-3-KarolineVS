### 1. Simulate Daily Demand and Analyze Results
# Write a function that simulates the daily demand for the product over the next n days using a Poisson distribution.
# **Steps:**
# -  Assume the average daily demand (`λ`) is 20 units.
# -  Use `numpy` to generate Poisson-distributed daily demand for n days.
# **Analyze the Results:**
# - Calculate and print the following statistics from the simulation results:
#   - Mean (average) daily demand
#   - Standard deviation
#   - 5th percentile (to understand the lower bound in a worst-case scenario)
#   - 95th percentile (to understand the upper bound in a best-case scenario)
# - Interpret the results in the context of inventory management.

import numpy as np
import random 

def simulate_demand(n, L, seed):
    '''simulate daily demand for n days'''
    demandList = []
    np.random.seed(seed)
    for day in range(n):
        dailyDemand = np.random.poisson(L) # Poisson distribution with lambda 20
        demandList.append(dailyDemand)
    return demandList

def results_function(demand, n):
    '''results of simulation'''
    sum = sum(demand) # demand for a month
    avg = np.mean(demand)
    std = np.std(demand)
    percentileFIVE = np.percentile(demand, 5)
    percentileNINE = np.percentile(demand, 95)
    #print(f"The mean is: {avg} \nThe standard deviation is: {std:.2f} \nThe 5%-percentile is: {percentileFIVE} \nThe 95%-percentile is: {percentileNINE}")
    return sum

### 2. Inventory Level Simulation
# Determine the optimal inventory level for one month that minimizes the risk of stockouts (running out of stock). Assume that there is no reordering during a month.
# **Steps:**
# - Assume the company wants to maintain a service level of 95%, meaning they want to meet the demand 95% of the time.
# - Simulate the total demand for 30 days multiple times (e.g., 1,000 simulations) to understand the distribution of monthly demand.
# - Determine the inventory level that would be sufficient to meet the demand 95% of the time.
# - Calculate and print the optimal inventory level.

def simulate_multiple_function(n,L,m,S):
    MonthlyDemandList = []
    #for run in range(m):
    for seed in range(1,1000):
        demand = simulate_demand(n, L, seed)
        total = sum(demand)
        MonthlyDemandList.append(total)
    InventoryLevel = np.percentile(MonthlyDemandList, S)
    print(f"The inventory should be {InventoryLevel:.2f}")

def get_input():
    print('Hi, please enter inputs. ')
    n = int(input("For how many days do you want to simulation?\n"))
    L = int(input("what is your avg daily sales? \n"))
    S = int(input("what is your service level? \n"))
    return n, L, S

n, L, S = get_input()
m=1000
# exercise 1
# demand = simulate_demand(n)
# sum = results_function(demand, n)

# exercise 2

simulate_multiple_function(n,L,m,S)

