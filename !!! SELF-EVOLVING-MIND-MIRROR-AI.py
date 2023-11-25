import random
from deap import base, creator, tools

# Define a fitness function (to be maximized)
def fitness_function(individual):
    return sum(individual),  # Return as a tuple

# Create the necessary DEAP structures
creator.create("FitnessMax", base.Fitness, weights=(1.0,))
creator.create("Individual", list, fitness=creator.FitnessMax)

toolbox = base.Toolbox()
toolbox.register("attr_bool", random.randint, 0, 1)
toolbox.register("individual", tools.initRepeat, creator.Individual, toolbox.attr_bool, n=10)
toolbox.register("population", tools.initRepeat, list, toolbox.individual)

toolbox.register("mate", tools.cxTwoPoint)
toolbox.register("mutate", tools.mutFlipBit, indpb=0.05)
toolbox.register("select", tools.selTournament, tournsize=3)
toolbox.register("evaluate", fitness_function)

# Create initial population
population = toolbox.population(n=50)

# Evolutionary process (number of generations)
for gen in range(20):
    offspring = algorithms.varAnd(population, toolbox, cxpb=0.5, mutpb=0.1)
    
    fits = toolbox.map(toolbox.evaluate, offspring)
    for fit, ind in zip(fits, offspring):
        ind.fitness.values = fit
    
    population = toolbox.select(offspring, k=len(population))

# Retrieve the best individual from the final population
best_individual = tools.selBest(population, k=1)[0]
print("Best Individual:", best_individual)
print("Fitness:", best_individual.fitness.values[0])
