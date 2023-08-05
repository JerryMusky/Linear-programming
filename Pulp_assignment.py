# -*- coding: utf-8 -*-
"""
Created on Sun Jul  9 16:04:48 2023

@author: Pei Ren
"""

from pulp import LpProblem, LpVariable, LpInteger, LpMaximize

# Create the problem instance
problem = LpProblem("Resource Allocation Optimization", LpMaximize)

# Define the decision variables
x1 = LpVariable("Smartphone", lowBound=0, cat=LpInteger)
x2 = LpVariable("Tablet", lowBound=0, cat=LpInteger)
x3 = LpVariable("Laptop", lowBound=0, cat=LpInteger)

# Define the objective function (profit)
problem += 900 * x1 + 1000 * x2 + 1400 * x3
#prices of: Smartphone = $900, Tablet = $1000, Laptop= $1400

# Define the constraints
problem += 1 * x1 + 2 * x2 + 3 * x3 <= 150  # Plastic materials constraint
problem += 1 * x1 + 2 * x2 + 4 * x3 <= 170  # Microchips constraint
problem += x1 + x2 + x3 <= 70  #Production capacity constraint

# Solve the problem
problem.solve()

# Print the optimal solution
print("Optimal Production Plan:")
print(f"Smartphone: {x1.varValue}")
print(f"Tablet: {x2.varValue}")
print(f"Laptop: {x3.varValue}")
print(f"Total Profit: {problem.objective.value()} dollars")

