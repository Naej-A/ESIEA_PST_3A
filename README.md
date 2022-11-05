# Activer un environnement virtuel
```shell
source <nom_env_virtuel>/bin/activate
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