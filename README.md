# Developpez_une_architecture_back-end_securisee_en_utilisant_Django_ORM
[**Projet 12** du parcours OpenClassrooms Développeur d'application - Python](https://course.oc-static.com/projects/Python+FR/840+D%C3%A9veloppez+une+architecture+back-end+s%C3%A9curis%C3%A9e/Ancienne+Version-De%CC%81veloppez+une+architecture+back-end+se%CC%81curise%CC%81e+en+utilisant+Django+ORM.pdf)

[![forthebadge](https://forthebadge.com/images/badges/made-with-python.svg)](https://forthebadge.com)

[![Flake8 Status](./reports/flake8/flake8-badge.svg?dummy=8484744)](reports/flake8/index.html)

Une application de gestion de la relation client (CRM), qui effectue le suivi de tous les clients et événements :
* L'application permettra essentiellement à l'equipe de suivre des clients, de leur ajouter des contracts, associés à des événements.
* L'applications exploitera **les points de terminaison d'API qui serviront les données**, ou le site d'admin de django.
* Principales fonctionnalités de l'application (autre que celle :
  - Authentification JWT des utilisateurs.
  - Permissions;Il est interdit à tout utilisateur autorisé autre que les membres de l'équipe associé au contrat et événements, d'émettre des requêtes d'actualisation.
  - L'équipe des gestionnaires sont les seuls capable à pouvoir supprimer, via le site d'admin de django.
  - respecte les normes OWASP et RGPD. 


### Prérequis
* [Python v3.x+](https://www.python.org/downloads/) .
* [PostGreSql](https://www.postgresql.org/download/). (configuration voir ci-dessous)
* Git installé (conseillé)

# INSTALLATION ( pour windows )


Créer un dossier vide. Il contiendra le code complet du projet
## *1. Installation du site*

Ouvrez un terminal:

Depuis le dossier précédemment créé, clonez le repository du programme avec la commande :

<pre><code>git clone https://github.com/Nathom78/Developpez_une_architecture_back-end_securisee_en_utilisant_Django_ORM.git</code></pre>

Ou utiliser [ce repository](https://github.com/Nathom78/Developpez_une_architecture_back-end_securisee_en_utilisant_Django_ORM.git) en téléchargeant le zip.
<br>


## *2. Installer un environnement python*

D'abord créer à partir de la racine du projet un environnement, ici appellé ".env"

`PS D:\..\> python -m venv .env`

Ensuite activer l'environnement python: 

`PS D:\..\> .env\Scripts\activate.ps1`


## *3. Installer les paquets nécessaires aux projets.*

<br>
Taper la commande suivante : 
<pre><code>
pip install -r requirements.txt
</code></pre>

Pour vérifier, taper cette commande :
<pre><code>pip list</code></pre>
Et vous devriez avoir :
<pre><code>Package                       Version
----------------------------- --------
asgiref                       3.7.2
attrs                         23.1.0
certifi                       2023.5.7
charset-normalizer            3.2.0
click                         8.1.6
colorama                      0.4.6
Django                        4.2.3
djangorestframework           3.14.0
djangorestframework-simplejwt 5.2.2
drf-spectacular               0.26.4
idna                          3.4
inflection                    0.5.1
Jinja2                        3.1.2
jsonschema                    4.18.4
jsonschema-specifications     2023.7.1
MarkupSafe                    2.1.3
mccabe                        0.7.0
Pillow                        10.0.0
pip                           23.2.1
psycopg                       3.1.9
psycopg-binary                3.1.9
pycodestyle                   2.10.0
pyflakes                      3.0.1
Pygments                      2.15.1
PyJWT                         2.8.0
pyrsistent                    0.19.3
pytz                          2023.3
PyYAML                        6.0
referencing                   0.30.0
requests                      2.31.0
rpds-py                       0.8.10
sentry-sdk                    1.28.1
setuptools                    68.0.0
sqlparse                      0.4.4
typing_extensions             4.7.1
tzdata                        2023.3
uritemplate                   4.1.1
urllib3                       2.0.3
wheel                         0.38.4
</code></pre>
## *4. configuration PostGreSql*
Utiliser les variables environments afin d'indiquer le chemin : (sinon utiliser les chemins par default)
- PGSERVICEFILE pour le fichier [.pg_service.conf](https://www.postgresql.org/docs/current/libpq-pgservice.html)
<pre><code>[My_db]
host=localhost
user=ThomasEpic
dbname=Epic
port=5432
</code></pre>
- PGPASSFILE pour le fichier [pgpass.conf](https://www.postgresql.org/docs/current/libpq-pgpass.html)
<pre><code>localhost:5432:Epic:ThomasEpic:ThomasAdmin</code></pre>

En Ayant par exemple [pgAdmin 4](https://www.pgadmin.org/download/) d'installé par ce lien, si la version installé par EDB ne fonctionne pas : 

Avec une base de donné crée comme *Epic*, en plus de celle de base *postgres*.

Avec un user avec les priviléges minimum ici *ThomasEpic* et son mot de passe *ThomasAdmin*.
## *5. Execution du logiciel*

Dans une fenêtre de terminal, se placer à la racine de l'application
ici Epic, ensuite taper les commandes suivantes :

Tout d'abord, nous devons appliquer les migrations à la base de donnée,
afin de pouvoir utiliser dans ce nouvel environnement, la base PostGreSql crée. 
<pre><code>
(.env) PS ~...\Epic> py manage.py migrate
</code></pre>

Ensuite, nous pouvons lancer l'application à travers le serveur Django.

<pre><code>
(.env) PS ~...\Epic py manage.py runserver 
</code></pre>

## *6. Urls avec drf-spectacular package*
### documentations de l'API
This exposes 3 endpoints:
- A YAML view of your API specification at /crm/schema/
- A swagger-ui view of your API specification at /crm/schema/swagger-ui/
- A ReDoc view of your API specification at /crm/schema/redoc/


## *7. Documentation Postman publique*
https://documenter.getpostman.com/view/21242674/2s9XxsVc52
***
# Technologies
<p>
<img src="https://skillicons.dev/icons?i=git,github,python,django,postgresql,postman&theme=dark">
</p>

![logo](https://www.django-rest-framework.org/img/logo.png)

***
## *Conventions de nommage et de codes :*
<p>PEP 8 – Style Guide for Python Code
<a href="https://peps.python.org/pep-0008/">ici</a>.
</p>

Un rapport **flake8** au format HTML est disponible dans le repertoire `\reports\flake8`, à la racine du projet.


