# Projet en Python 3.8

## Installation et lancement du projet (Linux et Mac)
Besoin de Python 3.8, le projet n'est pas garanti de fonctionner si une autre version est utilisé
```shell
source venv/bin/activate
which python  #vérifie quel python est utilisé
pip install -r requirements.txt
python app.py
```

# synopsys
Nous ésiarque avons volé cet immondice qu'est la boites aux lettres de l'estaca.
C'est voyous veulent la reprendre. Nous ferons tout ce qui est en notre pouvoir pour 
défendre 

## Pour la première fois d'un utilisateur 
Lire le ficher comment jouer 



## Désactiver un environnement virtuel
```shell
deactivate
```

# Lorsque des librairies ont été ajouté 
### Avant de push
```shell
pip freeze > requirements.txt
```
### Après un pull
```shell
cd /path/to/requirements.txt
pip install -r requirements.txt
```


# --------------- surement falloir le virer --------------

# Créer un executable
### 1- ajouter les images dans le fichier <nom_Exec>.spec
```python
a.datas += [('<relative Path>','<ABS Path>', 'Data')]
```
### 2- Créer l'executable
```shell
pyinstaller main.spec
```
### 3- Lancer l'executable
```shell
./dist/main 
```


