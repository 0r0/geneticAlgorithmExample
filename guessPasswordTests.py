import datetime
import unittest

import genetic


class GuessPasswordTests(unittest.TestCase):
    genSet: str = " abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!."

    def test_hello_world(self):
        target = "Hello World!"
        self.guess_password(target)

    def test_I_am_python_programmer(self):
        target = "I am  python programmer"
        self.guess_password(target)

    def guess_password(self, target):
        startTime = datetime.datetime.now()

        def FnGetFitness(genes):
            return get_fitness(genes, target)

        def FnDisplay(candidate: genetic.Chromosome):
            display(candidate, startTime)

        optimalFitness = len(target)
        best = genetic.get_best(FnGetFitness, len(target), optimalFitness, FnDisplay, self.genSet)
        self.assertEqual(best.Genes,target)
    def test_benchmark(self):
        genetic.Benchmark.run(self.test_I_am_python_programmer)


def get_fitness(genes: str, target):
    return sum(1 for expected, actual in zip(genes, target) if expected == actual)


def display(candidate: genetic.Chromosome, startTime):
    time_difference = datetime.datetime.now() - startTime
    print("{0}\t{1}\t{2}".format(candidate.Genes, candidate.Fitness, str(time_difference)))


if __name__ == "__main__":
    unittest.main()
