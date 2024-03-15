from sympy import factorint
# Part A-1 Total number of total combinations of the 2 dice
def count_combinations():
    count = 0
    for i in range(1, 7):
        for j in range(1, 7):
            count += 1
    return count

total_combinations = count_combinations()
print("Part A-1: Total combinations Possible:", total_combinations)

# Part A-2: Distribution of the total combinations of the 2 dice
def totalcombinations_distribution():
    combination = [] 
    count = 0
    for i in range(1, 7):
        dice = []  
        for j in range(1, 7):
            count +=1
            dice.append((i, j))
        combination.extend(dice)
    return combination
    
print("\nPart A-2: Distribution of possible combinations of Dice A and Dice B: ",totalcombinations_distribution())

# Part A-3: Possible Sum and Probability of the Sum
def calculate_probability_of_sums():
    combinations = totalcombinations_distribution()
    sum_frequency = {}
    total_combinations = len(combinations)

    for roll in combinations:
        sum_of_roll = sum(roll)
        if sum_of_roll in sum_frequency:
            sum_frequency[sum_of_roll] += 1
        else:
            sum_frequency[sum_of_roll] = 1

    probability_of_sums = {}
    for key, value in sum_frequency.items():
        probability_of_sums[key] = value / total_combinations

    return probability_of_sums

# Part B: Reattach the spots
def calculate_spot_distribution():
    original_probabilities = {
        2: 1, 3: 2, 4: 3, 5: 4, 6: 5, 7: 6, 8: 5, 9: 4, 10: 3, 11: 2, 12: 1
    }

    common_denominator = 36
    new_dice_spots = {}

    for sum_value, probability in original_probabilities.items():
        product = probability * common_denominator
        factors = factorint(product)
        spots = {factor: 0 for factor in factors}

        # Distribute the factors across the faces of the new dice
        remaining = product
        for factor in factors:
            while remaining % factor == 0 and spots[factor] < 6:
                spots[factor] += 1
                remaining //= factor

        new_dice_spots[sum_value] = spots

    return new_dice_spots

# Part A-3: Possible Sum and Probability of the Sum
probabilities = calculate_probability_of_sums()
for key, value in probabilities.items():
    print("\nPossible Sum:", key, "\nProbability of the sum:", value)

# Part B: Calculate and print spot distribution
new_dice_spots = calculate_spot_distribution()
for sum_value, spots in new_dice_spots.items():
    print(f"\nSum = {sum_value}: {spots}")
