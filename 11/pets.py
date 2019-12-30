from flask import Flask
import pets_functions

app = Flask(__name__)
app.config["DEBUG"] = True


@app.route("/")
def index():
    return pets_functions.get_homepage()

@app.route("/instructions/")
def instructions():
    return pets_functions.get_instructions()

@app.route("/pets/")
def pets():
    return pets_functions.get_pets()

@app.route("/pets/<pet>/")
def pet_detail(pet):
    return pets_functions.get_pet_detail(pet)

if __name__ == "__main__":
    app.run()
