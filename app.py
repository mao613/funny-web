from flask import Flask
import random

app = Flask(__name__)

jokes = [
    "What can you do if you cannot push your git changes? Use the --force, Luke",
    "Which body part does a programmer know best? ARM",
    "Relationship status? I'll leave the relations to the database.",
    "How do you get the code for the bank vault? You checkout their branch.",
    "How did the developer announce their engagement? They returned true!"]

@app.get("/")
def tell_a_joke():
    joke = random.choice(jokes)
    return f"<p>{joke}</p>"

