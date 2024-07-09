import itertools

# Creating a dictionary with lists of letters
letter_dict = {
    '1': ['a', 'b'],
    '2': ['c', 'd'],
    '3': ['e', 'f']
}

# Generating all combinations of letters
combinations = list(itertools.product(*letter_dict.values()))

# Displaying the combinations
print("All combinations of letters:")
for combination in combinations:
    print(''.join(combination))
