animals = {"Nemo": "fish", "Charlie": "dog", "Minnie": "mouse", "Oliver": "cat"}

def for_loop(dictionary):
    for key, value in dictionary.items():
        print(f"{key} is {value}.")
    print()

for_loop(animals)
animals["Minnie"] = "snake"
for_loop(animals)
animals["Roger"] = "parrot"
for_loop(animals)
del animals["Nemo"]
for_loop(animals)