# ---------------------------------------------------------------
#  Mon premier site Web avec Flask
# ---------------------------------------------------------------
#  Ce fichier est le "cerveau" de votre site : c'est lui qui
#  reçoit les demandes des navigateurs et qui fabrique les réponses.
#
#  Vous allez le compléter petit à petit, exercice après exercice.
#  Les consignes sont dans le dossier "exercices/".
# ---------------------------------------------------------------

from flask import Flask, render_template, render_template_string, request, abort
from datetime import datetime
from zoneinfo import ZoneInfo

app = Flask(__name__)


# Une "route" associe une adresse (URL) à une fonction Python.
# Ici : quand quelqu'un visite la page d'accueil "/",
# Flask exécute la fonction accueil() et renvoie son résultat au navigateur.
@app.get("/")
def accueil():
    return render_template("accueil.html")


# ---------------------------------------------------------------
#  Ajoutez vos nouvelles routes ci-dessous 👇
# ---------------------------------------------------------------
@app.get("/bonjour/<prenom>")
def bonjour(prenom):
    # Le prénom est extrait directement de l'URL.
    return f"<h1>Bonjour {prenom} !</h1>"


# Affiche la page de présentation avec des informations transmises au template.
@app.get("/presentation")
def presentation():
    return render_template("presentation.html", prenom="Léa", nom="Martin",
                       loisirs=["Jeux vidéo", "Musique", "Escalade"])


# Génère une liste HTML à partir des loisirs fournis au template.
@app.get("/loisirs")
def loisirs():
    return render_template_string("""
<ul>
{% for loisir in loisirs %}
    <li>{{ loisir }}</li>
{% endfor %}
</ul>
""", loisirs=["Jeux vidéo", "Musique", "Escalade"])


# Additionne les nombres a et b fournis dans les paramètres de l'URL.
@app.get("/calcul")
def calcul():
    a = int(request.args.get("a", 0))
    b = int(request.args.get("b", 0))
    return f"{a} + {b} = {a + b}"


# Affiche le formulaire qui enverra ses données à la route /salut.
@app.get("/formulaire")
def formulaire():
    return render_template("formulaire.html")


# Traite les données du formulaire (POST) ou les paramètres de l'URL (GET).
@app.route("/salut", methods=["GET", "POST"])
def salut():
    if request.method == "POST":
        prenom = request.form.get("prenom", "inconnu")
        ville = request.form.get("ville", "nulle part")
    else:
        prenom = request.args.get("prenom", "inconnu")
        ville = request.args.get("ville", "nulle part")
    return f"Bonjour {prenom}, qui vient de {ville} ! (reçu en {request.method})"


# 3xx : une redirection
@app.get("/home")
def home():
    return redirect("/")


# 4xx : un accès interdit
@app.get("/secret")
def secret():
    # Déclenche l'erreur 403, traitée par le gestionnaire ci-dessous.
    abort(403)


# Affiche le template personnalisé lorsqu'une URL n'existe pas.
@app.errorhandler(404)
def page_introuvable(erreur):
    return render_template("404.html"), 404


# Affiche le template personnalisé lorsqu'une page est interdite.
@app.errorhandler(403)
def acces_interdit(erreur):
    return render_template("403.html"), 403

@app.get("/moi")
def moi():
    return render_template(
        "moi.html",
        ip=request.headers.get("X-Real-IP", request.remote_addr),
        navigateur=request.headers.get("User-Agent"),
        langues=request.headers.get("Accept-Language"),
        entetes=request.headers,
    )

@app.get("/api/heure")
def api_heure():
    maintenant = datetime.now(ZoneInfo("Europe/Paris"))
    return jsonify({
        "heure": maintenant.strftime("%H:%M:%S"),
        "date": maintenant.strftime("%d/%m/%Y"),
        "message": "Bonjour depuis mon API !",
    })
# ---------------------------------------------------------------
#  Ne pas modifier : utile seulement pour lancer le site
#  sur votre propre ordinateur (python flask_app.py)
# ---------------------------------------------------------------
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
