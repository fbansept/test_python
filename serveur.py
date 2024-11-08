from flask import Flask, render_template

app = Flask(__name__)

class Article :
    def __init__(self, url_image, label, texte):
        self.url_image = url_image
        self.label = label
        self.texte = texte

articles = (
    Article("https://placehold.co/600x400?text=natation", "natation", " Finale 400m 4 nages (H) | Natation | Jeux Olympiques de Paris 2024"), 
    Article("https://placehold.co/600x400?text=judo", "Judo", "Finales par équipe mixte | Judo | Jeux Olympiques de Paris 2024"), 
    Article("https://placehold.co/600x400?text=triathlon", "Triathlon", " Triathlon (F) | Jeux Olympiques de Paris 2024 FRA v POL - Finale(H) | Volleyball | Jeux Olympiques de Paris 2024 Volleyball FRA v"), 
)

@app.route("/")
def accueil():
    return render_template("accueil.html", articles = articles)
