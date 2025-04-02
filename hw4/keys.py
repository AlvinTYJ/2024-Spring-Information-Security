import itertools
import string

# Key template
key_template = '*-?5Q*E*qeDe*%Bs'

# Extract positions of '*' in the key template
stars_indices = [i for i, char in enumerate(key_template) if char == '*']
num_stars = len(stars_indices)

# Printable characters
printable_chars = string.printable

# Iterate over all combinations of printable characters for the '*' positions
for replacement in itertools.product(printable_chars, repeat=num_stars):
    # Create a new key by replacing '*' with the current combination
    key = list(key_template)
    for index, char in zip(stars_indices, replacement):
        key[index] = char
    key = ''.join(key).ljust(16, '\x00')  # Pad to 16 bytes

    # Print the resulting key
    print("Generated Key:", key)

print("All possible keys have been generated.")
