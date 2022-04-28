1 pip install -r requirements.txt installer les dépendances

2 Ouvrir l'invite de commandes et se rendre dans ce dossier (chemin d'accès à ce dossier)
  Ou à partir de ce dossier faire clique droit et ouvrir une invite de commande

3 taper la commande ".\venv\scripts\activate" pour activer l'environnement virtuel de python

4 taper la commande "uvicorn main:app --reload" pour lancer fastApi sur le localhost

5 ouvrir un navigateur web puis taper dans la barre de url "localhost:numéro port"
  généralement il s'execute sur le port 8000, si c'est le cas l'url sera "localhost:8000/docs" ou "http://127.0.0.1:8000/docs"