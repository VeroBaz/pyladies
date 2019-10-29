# Sort a given list alphabetically according to the second letter of each item
animals = ["dog", "cat", "rabbit", "snake", "fish", "elephant"]

# Generate keys = second letter of the animal
keys = []
for animal in animals:
    keys.append(animal[1])

# Create tuples of key and the animal and sort it
sorted_animals = sorted(list(zip(keys, animals)))

# Generate the new list with sorted animals
result = []
for item in sorted_animals:
    result.append(item[1])
print(result)