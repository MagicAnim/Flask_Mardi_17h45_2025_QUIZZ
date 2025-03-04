# On importe Flask du module flask
from flask import Flask, render_template, session

# Importation de os
import os

# On importe la liste de dictionnaires (question + réponses) de notre fichiers questions.py
from questions import questions

# CREATION DE l'APP
# On crée une instance de Flask qui est donc notre app qu'on stocke dans la variable app
app = Flask("Mon Super Quizz")
app.secret_key = os.urandom(24)

# Route de notre page d'accueil qui est donc à la racine de notre app
@app.route("/")
def index():
    session["numero_question"] = 0
    session["score"] = { "Pikachu" : 0, "Mew" : 0, "Salamèche" : 0, "Carapuce":0}
    return render_template("index.html")

# Route seconde Page
@app.route("/question")
def question():
    # On accède à la variable global questions
    global questions
    # On récupère le numéro de la question
    numero = session["numero_question"]
    # On vérifie que nous en sommes pas à la dernière
    if numero < len(questions):
        # On récupère l'énoncé de la question
        question = questions[numero]["enonce"]
        # On crée une copie du dictionnaire de notre question
        questions_copy = questions[numero].copy()
        # On supprime l'énoncé pour n'avoir que les questions
        questions_copy.pop("enonce")
        # On récupère nos réponses sous forme de liste
        reponses = list(questions_copy.values())
        # On récupère les clefs = personnages sous forme de liste pour comptage des scores
        clefs = list(questions_copy.keys())
        # On stocke l'ordre dans un cookie pour le comptage des scores
        session["clefs"] = clefs

        return render_template("question.html", question = question, reponses = reponses)

# Route permettant de compter les réponses de l'utilisateur
# @app.route("/reponse/<numero>")


# EXECUTION
# host = "0.0.0.0" -> app accessible par n'importe quelle adresse
# port = 81 -> port d'écoute du serveur de l'app
app.run(host = "0.0.0.0", port = 81)