import random

def generate_numbers_summing_to(total, count):
    numbers = []
    remaining_total = total

    # Generate random numbers
    for _ in range(count - 1):
        number = random.uniform(0, remaining_total)
        numbers.append(number)
        remaining_total -= number

    # Add the last number to ensure the sum is equal to the total
    numbers.append(remaining_total)

    return numbers
if __name__ == '__main__':
    # Example usage
    total_amount = 0.1
    number_count = 5

    result = generate_numbers_summing_to(total_amount, number_count)
    print(result)
    print(sum(result))