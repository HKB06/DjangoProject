Django Exercise - Mini Blog Application

Objectif
Ce projet implémente une application de blog minimaliste en utilisant Django et le modèle MVT (Model-View-Template). L'application permet de gérer des articles et leurs commentaires avec une interface simple et moderne.

Fonctionnalités
Articles :
Créer, modifier, afficher et supprimer des articles.

Commentaires :
Ajouter, modifier et supprimer des commentaires sur les articles.

Navigation :
Interface utilisateur claire avec des liens pour naviguer entre les pages.

Structure du projet

Modèles :
BlogPost : Représente les articles.
Comment : Représente les commentaires liés aux articles.

Templates :
Pages organisées dans templates/blog/, incluant :
post_list.html (liste des articles).
post_detail.html (détails d’un article et ses commentaires).
create_post.html (création d’un article).
edit_post.html (édition d’un article).
add_comment.html et edit_comment.html (gestion des commentaires).

Dossier statique :
Fichiers CSS dans static/blog/styles.css.


Routes principales
Articles
Liste des articles : /
Détails d’un article : /post/<id>/
Créer un article : /post/create/
Modifier un article : /post/<id>/edit/
Supprimer un article : /post/<id>/delete/

Commentaires
Ajouter un commentaire : /post/<id>/add_comment/
Modifier un commentaire : /comment/<id>/edit/
Supprimer un commentaire : /comment/<id>/delete/
Installation

1. Cloner le projet
git clone <lien_du_dépôt>
cd <nom_du_projet>

2. Configurer l’environnement
python -m venv env
source env/bin/activate  # Sous Linux/macOS
.\env\Scripts\activate   # Sous Windows
pip install -r requirements.txt

3. Initialiser la base de données
python manage.py makemigrations
python manage.py migrate

4. Créer un superutilisateur
python manage.py createsuperuser

5. Lancer le serveur
python manage.py runserver

Accédez à l’application via http://127.0.0.1:8000/.


Tests
Lancer les tests
Exécutez les tests unitaires pour vérifier les fonctionnalités principales :
python manage.py test

Tests inclus
Création, modification et suppression d’articles.
Ajout, modification et suppression de commentaires.
Vérification des redirections et du rendu des templates

Fait par Hugo khaled Brotons Et Nail Benamer
