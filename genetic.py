import random

def _generate_parent(length,genSet):
    genes = []
    while len(genes) < length:
        sampleSize = min(length - len(genes), len(genSet))
        genes.extend(random.sample(genSet, sampleSize))
    return ''.join(genes)



def _mutate(parent: str,genSet):
    index = random.randrange(0, len(parent))
    childGenes = list(parent)
    newGene, alternate = random.sample(genSet, 2)
    childGenes[index] = alternate if newGene == childGenes[index] else newGene
    return ''.join(childGenes)


def get_best(get_fitness,lenTarget,optimalFitness,display,genSet):
    random.seed()

    bestParent = _generate_parent(lenTarget,genSet)
    bestFitness = get_fitness(bestParent)
    display(bestParent)
    if bestFitness >= optimalFitness:
        return bestParent
    while True:
        child = _mutate(bestParent,genSet)
        childFitness = get_fitness(child)
        if bestFitness >= childFitness:
            continue
        display(child)
        if childFitness >= optimalFitness:
            return child
        bestFitness = childFitness
        bestParent = child