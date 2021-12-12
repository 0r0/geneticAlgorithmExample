import datetime
import genetic

def test_hello_world():
    target="Hello World!"
    guess_password(target)

def guess_password(target):
    genSet:str=" abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!."
    startTime=datetime.datetime.now()
    def FnGetFitness(genes):
        return get_fitness(genes,target)
    def FnDisplay(genes):
        display(genes,target,startTime)
    optimalFitness=len(target)
    genetic.get_best(FnGetFitness,len(target),optimalFitness,FnDisplay,genSet)


def get_fitness(genes: str,target):
    return sum(1 for expected, actual in zip(genes, target) if expected == actual)

def display(genes,target,startTime):
    time_difference = datetime.datetime.now() - startTime
    fitness = get_fitness(genes,target)
    print("{0}\t{1}\t{2}".format(genes, fitness, str(time_difference)))


if __name__=="__main__":
    test_hello_world()
