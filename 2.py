import random

def get_numbers_ticket(min, max, quantity):
    if min < 0 or max > 1000 or quantity > max - min:
        return []
    return sorted(random.sample(range(min, max), quantity))

lottery_numbers = get_numbers_ticket(1, 49, 6)
print("Ваші лотерейні числа:", lottery_numbers)