import json
from flask import abort

def get_homepage():
    homepage_text = """
        Welcome to pets lending website!\n\n
        Have you ever wanted to try how it is to have a pet?
        Do you temporary need a specific pet?
        Do you want to test your children whether they are ready
        to take care of a pet before buying one?\n\n
        You are on the right website!
        """
    return homepage_text

def get_instructions():
    instructions_text = """
        How it works?\n\n
        1. Pick a pet\n
        2. Contact the owner\n
        3. Enjoy your new pet!
        """
    return instructions_text

def get_data():
    with open("pets_data.txt", encoding = "utf-8") as file_:
        data = json.load(file_)
    return data

def get_pets():
    pets = sorted(get_data().keys())
    return str(pets)[1:-1]

print(get_pets())

def get_pet_detail(pet):
    list_of_pets = get_data().keys()
    if pet not in list_of_pets:
        return abort(404)
    else:
        return get_data()[pet]
