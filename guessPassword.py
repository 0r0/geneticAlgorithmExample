import random
import datetime
# Genes
genSet = " abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!."
target = "Hello World!"


# Generate a Guess
def generate_parent(length):
    genes = []
    while len(genes) < length:
        sampleSize = min(length - len(genes), len(genSet))
        genes.extend(random.sample(genSet, sampleSize))
        return ''.join(genes)


# fitness
def get_fitness(guess: str):
    return sum(1 for expected, actual in zip(guess, target) if expected == actual)


# mutate
def mutate(parent: str):
    index = random.randrange(0, len(parent))
    childGenes = list(parent)
    newGene, alternate = random.sample(genSet, 2)
    childGenes[index] = alternate if newGene == childGenes[index] else newGene
    return ''.join(childGenes)

#display
def display(guess):
    time_difference=datetime.datetime.now()-startTime
    fitness=get_fitness(guess)
    print("{0}\t{1}\t{3}".format(guess,fitness,time_difference))



startTime=datetime.datetime.now()