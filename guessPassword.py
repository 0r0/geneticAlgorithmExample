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






