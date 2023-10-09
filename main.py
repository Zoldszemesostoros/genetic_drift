import random;
import collections

DICE_SIDES = 6;


def main():
    pretty_print_frequencies(simulation(3, 10000, 0))

def pretty_print_frequencies(frequencies):
    total_frequencies = sum(frequencies.values())
    hightest_iteration_count = list(frequencies.keys())[-1]
    for i in range(hightest_iteration_count):
        frequency = frequencies[i] if i in frequencies.keys() else 0
        hashtag_count = int((float(frequency)/total_frequencies) * 200)
        
        print("{}\t|{}".format(i, "#" * hashtag_count))

def simulation(dice_count, number_of_tries, printing_level):
    iteration_counts = []
    for _ in range(number_of_tries):
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

main()
