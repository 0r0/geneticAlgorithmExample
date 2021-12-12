import random
#Genes
genSet=" abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!."
target="Hello World!"

#Generate a Guess
def generate_parent(length):
    genes=[]
    while len(genes)<length:
        sampleSize=min(length-len(genes),len(genSet))
        genes.extend(random.sample(genSet,sampleSize))
        return ''.join(genes)

 #fitness
def get_fitness(guess:str):
    return sum(1 for expected,actual in zip(guess,target) if expected==actual)





