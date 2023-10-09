import random;

def fixed(alleles):
    return len(set(alleles)) == 1

def genetic_drift(alleles, printing_level):
    result = []
    length = len(alleles)
    for _ in range(length):
        dice_throw = random.randrange(length)
        result.append(alleles[dice_throw])
        if printing_level >= 2:
            print(dice_throw + 1, end=", ")
    return result

def test_1dice(printing_level):
    alleles = ["A", "B", "C", "D", "E", "F"]
    if printing_level >= 2:
        print(alleles)
    required_iterations = 0
    while not fixed(alleles):
        alleles = genetic_drift(alleles, printing_level)
        required_iterations += 1
        if printing_level >= 2:
            print(alleles)
    if printing_level >= 1:
        print("Required iterations: {}".format(required_iterations))
    return required_iterations

test_1dice(2)
