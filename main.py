import random;
import collections

DICE_SIDES = 6;

def do_experiment(dice_count, test_count, printing_level):
    print("Number of dices: ", dice_count)
    print("Number of tests: ", test_count)
    pretty_print_frequencies(simulation(dice_count, test_count, printing_level))

def pretty_print_frequencies(frequencies):
    total_frequencies = sum(frequencies.values())
    hightest_iteration_count = list(frequencies.keys())[-1]
    for i in range(hightest_iteration_count):
        frequency = frequencies[i] if i in frequencies.keys() else 0
        hashtag_count = int((float(frequency)/total_frequencies) * 400)
        
        print("{}\t|{}".format(i, "#" * hashtag_count))

def simulation(dice_count, test_count, printing_level):
    iteration_counts = []
    for _ in range(test_count):
        iteration_counts.append(test(dice_count, printing_level))
    frequencies = dict(collections.Counter(iteration_counts))
    sorted_frequencies = collections.OrderedDict(sorted(frequencies.items()))
    return sorted_frequencies
    
def test(dice_count, printing_level):
    alleles = list(range(dice_count * DICE_SIDES))
    if printing_level >= 2:
        print(alleles)
    iterations_to_fixation = 0
    while not fixed(alleles):
        alleles = genetic_drift(alleles, dice_count, printing_level)
        iterations_to_fixation += 1
        if printing_level >= 2:
            print(alleles)
    if printing_level >= 1:
        print("Required iterations: {}".format(iterations_to_fixation))
    return iterations_to_fixation

def fixed(alleles):
    return len(set(alleles)) == 1

def genetic_drift(alleles, dice_count, printing_level):
    result = []
    length = len(alleles)
    for _ in range(length):
        dice_throw = 0
        for _ in range(dice_count):
            dice_throw += random.randrange(DICE_SIDES)
        result.append(alleles[dice_throw])
        if printing_level >= 2:
            print(dice_throw + 1, end=", ")
    return result

do_experiment(1, 100000, 0)
do_experiment(2, 100000, 0)
