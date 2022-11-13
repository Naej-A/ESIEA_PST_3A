# Projet en Python 3.8

# Activer un environnement virtuel
```shell
source venv/bin/activate
which python  #vérifie quel python est utilisé
```
# Désactiver un environnement virtuel
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


