# ---------------------------------------------------------------
#  Mon premier site Web avec Flask
# ---------------------------------------------------------------
#  Ce fichier est le "cerveau" de votre site : c'est lui qui
#  reçoit les demandes des navigateurs et qui fabrique les réponses.
#
#  Vous allez le compléter petit à petit, exercice après exercice.
#  Les consignes sont dans le dossier "exercices/".
# ---------------------------------------------------------------

# Importation des modules nécessaires.
# Flask permet de créer l'application web.
# render_template sert à afficher des fichiers HTML dans templates/.
# request permet de lire les données envoyées par le navigateur.
# abort permet de déclencher des erreurs HTTP (403, 404, etc.).
# redirect permet de rediriger vers une autre URL.
# jsonify permet de renvoyer des données JSON depuis une API.
from flask import Flask, render_template, render_template_string, request, abort, redirect, jsonify

# escape permet d'échapper les caractères HTML pour éviter les injections.
from markupsafe import escape

# datetime et ZoneInfo sont utilisés pour afficher l'heure en Europe/Paris.
from datetime import datetime
from zoneinfo import ZoneInfo

# Création de l'application Flask.
# __name__ correspond au nom du fichier courant.
app = Flask(__name__)


# Une "route" associe une adresse (URL) à une fonction Python.
# Ici : quand quelqu'un visite la page d'accueil "/",
# Flask exécute la fonction accueil() et renvoie son résultat au navigateur.
# Route principale : page d'accueil.
# Quand on visite "/", Flask appelle cette fonction et renvoie la page accueil.html.
@app.get("/")
def accueil():
    return render_template("accueil.html")


# ---------------------------------------------------------------
#  Ajoutez vos nouvelles routes ci-dessous 👇
# ---------------------------------------------------------------
# Route dynamique : /bonjour/<prenom>
# Le prénom est récupéré directement dans l'URL.
# Exemple : /bonjour/Emma
@app.get("/bonjour/<prenom>")
def bonjour(prenom):
    # escape(...) empêche les balises HTML ou scripts dangereux.
    return f"<h1>Bonjour {escape(prenom)} !</h1>"


# Route /presentation : affiche une page HTML avec des variables envoyées au template.
# Le template presentation.html reçoit des valeurs : prenom, nom, loisirs.
@app.get("/presentation")
def presentation():
    return render_template("presentation.html", prenom="Léa", nom="Martin",
                       loisirs=["Jeux vidéo", "Musique", "Escalade"])


# Route /loisirs : génère du HTML directement dans Python avec render_template_string.
# La boucle {% for %} affiche chaque élément de la liste dans une balise <li>.
@app.get("/loisirs")
def loisirs():
    return render_template_string("""
<ul>
{% for loisir in loisirs %}
    <li>{{ loisir }}</li>
{% endfor %}
</ul>
""", loisirs=["Jeux vidéo", "Musique", "Escalade"])


# Route /calcul : lit des paramètres passés dans l'URL, par exemple ?a=5&b=7.
# On convertit en int pour faire une addition.
# Si la valeur n'est pas un nombre, on retourne une erreur HTTP 400.
@app.get("/calcul")
def calcul():
    try:
        a = int(request.args.get("a", 0))
        b = int(request.args.get("b", 0))
    except (TypeError, ValueError):
        return "Les paramètres 'a' et 'b' doivent être des nombres entiers.", 400
    return f"{a} + {b} = {a + b}"


# Route /formulaire : affiche la page HTML contenant un formulaire.
# Ce formulaire envoie ensuite les données vers /salut.
@app.get("/formulaire")
def formulaire():
    return render_template("formulaire.html")


# Route /salut : reçoit les données envoyées par le formulaire.
# On accepte aussi le mode GET pour tester avec des paramètres dans l'URL.
@app.route("/salut", methods=["GET", "POST"])
def salut():
    # Si la requête est en POST, on lit les données du formulaire.
    if request.method == "POST":
        prenom = request.form.get("prenom", "inconnu")
        ville = request.form.get("ville", "nulle part")
    else:
        # Sinon, on lit les paramètres de l'URL.
        prenom = request.args.get("prenom", "inconnu")
        ville = request.args.get("ville", "nulle part")

    # escape(...) sécurise l'affichage pour éviter les injections HTML/JS.
    return f"Bonjour {escape(prenom)}, qui vient de {escape(ville)} ! (reçu en {escape(request.method)})"


# Route /home : redirection HTTP 302 vers la page d'accueil.
# Cela sert à montrer le principe des redirections (code 3xx).
@app.get("/home")
def home():
    return redirect("/")


# Route /secret : simule une page interdite.
# abort(403) déclenche une erreur HTTP 403, gérée plus bas.
@app.get("/secret")
def secret():
    abort(403)


# Gestionnaire d'erreur 404 : lorsqu'une page n'existe pas.
@app.errorhandler(404)
def page_introuvable(erreur):
    return render_template("404.html"), 404


# Gestionnaire d'erreur 403 : lorsqu'un accès est interdit.
@app.errorhandler(403)
def acces_interdit(erreur):
    return render_template("403.html"), 403


# Route /moi : affiche des informations du navigateur et des en-têtes HTTP.
# request.headers contient les en-têtes envoyés par le navigateur.
@app.get("/moi")
def moi():
    return render_template(
        "moi.html",
        ip=request.headers.get("X-Real-IP", request.remote_addr),
        navigateur=request.headers.get("User-Agent"),
        langues=request.headers.get("Accept-Language"),
        entetes=request.headers,
    )


# Route API /api/heure : renvoie l'heure actuelle au format JSON.
# C'est une API simple, utilisée par des applications ou des pages JavaScript.
@app.get("/api/heure")
def api_heure():
    maintenant = datetime.now(ZoneInfo("Europe/Paris"))
    return jsonify({
        "heure": maintenant.strftime("%H:%M:%S"),
        "date": maintenant.strftime("%d/%m/%Y"),
        "message": "Bonjour depuis mon API !",
    })


# Route /horloge : affiche un template qui montre une horloge HTML/CSS/JS.
@app.get("/horloge")
def horloge():
    return render_template("horloge.html")


# ---------------------------------------------------------------
#  Ne pas modifier : utile seulement pour lancer le site
#  sur votre propre ordinateur (python flask_app.py)
# ---------------------------------------------------------------
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=False)
