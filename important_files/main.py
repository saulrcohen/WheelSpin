import random
from generate_random import generate_numbers_summing_to
from constants import min_max, target_value, best_percents

outcomes = ['Coins', 'Eggs', 'Hammer', 'Coconut', 'Free Spins', 'Gems', 'No Reward']
probabilities = [0.10, 0.15, 0.10, 0.10, 0.10, 0.10, 0.35]

subtypes = {
    'Coins': [250, 500, 750, 1000, 1500, 2500],
    'Eggs': ['Silver Egg', 'Gold Egg', 'Diamond Egg'],
    'Hammer': ['Bronze Hammer'],
    'Coconut': ['Coconut Item'],
    'Free Spins': ['Free Spin X1', 'Free Spin X2', 'Free Spin X3'],
    'Gems': [10, 25, 50, 75, 100]
}

economy_values = {
    'Coins': {250: .05,500:.1,750: .15,1000:.2,1500: .3,2500:.5},
    'Eggs': {'Silver Egg':.25, 'Gold Egg':.75, 'Diamond Egg':1.5},
    'Hammer': {'Bronze Hammer':.2},
    'Coconut': {'Coconut Item':.09},
    'Free Spins': {'Free Spin X1':.2, 'Free Spin X2':.4, 'Free Spin X3':.6},
    'Gems': {10:.1, 25:.25, 50:.5, 75:.75, 100:1},
    'No Reward': []  # Add an empty list for 'No Reward'
}

def generate_random_subprobability():
    subtype_probability = {
        'Coins': generate_numbers_summing_to(.1,6),
        'Eggs': generate_numbers_summing_to(.15,3),
        'Hammer': generate_numbers_summing_to(0.1,1),
        'Coconut': generate_numbers_summing_to(0.1,1),
        'Free Spins': generate_numbers_summing_to(0.1,3),
        'Gems': generate_numbers_summing_to(.1,5)
    }
    return subtype_probability


def get_empty_spins():
    random_count = random.randint(1, 3)
    numbers = []

    for _ in range(random_count):
        number = random.randint(0, 4)
        numbers.append(number)

    return numbers


def start_spin(vip_level, time_until_free_spin_eligible):
    min_value, max_value = min_max[vip_level]
    things_won, total_value, time_until_free_spin_eligible = spin_wheel(vip_level,
                                                                        time_until_free_spin_eligible=time_until_free_spin_eligible)
    while total_value < min_value or total_value > max_value or things_won.count('No Reward') > 3:
        things_won, total_value, time_until_free_spin_eligible = spin_wheel(vip_level,
                                                                            time_until_free_spin_eligible)
    return things_won, total_value, time_until_free_spin_eligible


def spin_wheel(vip_level, time_until_free_spin_eligible):
    empty_spin = get_empty_spins()
    i = 0
    total_eco_value = 0
    general_category_won = []
    things_won = []
    subtype_probability = best_percents[vip_level]

    while i < 5:
        if time_until_free_spin_eligible == 0:
            outcomes = ['Coins', 'Eggs', 'Hammer', 'Coconut', 'Gems', 'No Reward', 'Free Spins']
            probabilities = [0.10, 0.15, 0.10, 0.10, 0.10, 0.35, 0.10]
        else:
            outcomes = ['Coins', 'Eggs', 'Hammer', 'Coconut', 'Gems', 'No Reward']
            probabilities = [0.10, 0.15, 0.10, 0.10, 0.10, 0.35]
            time_until_free_spin_eligible -= 1

        symbol = random.choices(outcomes, weights=probabilities, k=1)[0]

        if i in empty_spin:
            symbol = 'No Reward'

        if symbol in list(subtypes.keys()):
            if symbol == 'Gems':
                index = outcomes.index('Gems')
                outcomes.remove('Gems')
                del probabilities[index]
            if symbol == 'Free Spins':
                time_until_free_spin_eligible = 10

            general_category_won.append(symbol)

            if general_category_won.count(symbol) > 1 and symbol != 'Gems':
                index = outcomes.index(symbol)
                del outcomes[index]
                del probabilities[index]

            lower_symbol = random.choices(subtypes[symbol], weights=subtype_probability[symbol], k=1)[0]
            eco_value = economy_values[symbol][lower_symbol]
            total_eco_value += eco_value

            if type(lower_symbol) == int:
                things_won.append(str(lower_symbol) + ' ' + symbol)
            else:
                things_won.append(lower_symbol)
        else:
            things_won.append('No Reward')

        i += 1

    return things_won, total_eco_value, time_until_free_spin_eligible


def run_monte_carlo():
    vip_levels = [1,2,3,4,5,6,7]
    best_percent_per_level = dict()
    for vip_level in vip_levels:
        num_of_iterations = 0
        best = 0
        target = .9
        smallest_difference = 1000
        while num_of_iterations < 600:
            i = 0
            answer = 0
            while i < 500:
                return_from_this_round, this_round_percentages = start_spin(vip_level, )
                i += 1
                answer += return_from_this_round
            answer = answer/i
            print(f'For these percentages, we got {answer}')
            if abs(answer - target) < smallest_difference:
                smallest_difference = abs(answer - target)
                best_percentages = this_round_percentages
            num_of_iterations += 1
        best_percent_per_level[vip_level] = best_percentages
