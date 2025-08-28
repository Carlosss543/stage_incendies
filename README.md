Pour créer le jeu de données final il faut lancer create_dataset_final.ipynb en spécifiant la valeur de split et de crop_size.
Il faut déjà avoir téléchargé le jeu de données data/dataset/split avec split égal à train, val ou test.

utils contient des fonctions auxiliaires et surtout un loader pytorch pour le jeu de donné. Il y a un exemple d'utilisation de ce loader à l'emplacement divers/loader.ipynb.



Les données sont dans le dossier data dont l'arborescence est :
    data
    ├─ dataset
    ├─ dataset_crops
    <!-- ├─ dataset_attributs
    ├─ dataset_crops_annotations
    ├─ dataset_crops_sat -->

Le dossier "create_datasets" contient des codes pour créer divers types de datasets qui m'ont été utiles au cours de ce projet.

Le dossier "divers" contient des codes qui m'ont permis de faire des tests à différentes étapes ainsi que des codes pour obtenir des informations sur le dataset.

Le dossier "interprétabilité" contient les différents modèles de l'architecture et des tests pour voir à quoi réagissent les neurones de la couche sparse du vae.

Le dossier "approche_concurrente" contient l'implémentation d'une approche concurrente qui consiste à utiliser le Resnet18 pour prédire les attributs puis à utiliser une couche linéaire pour passer des attributs aux classes. Ainsi la prédiction des attributs ne se fait plus de manière implicite mais explicite.

Le dossier "segmentation_semantique" contient tous les codes de segmentation sémantique et de traitement d'images que j'ai réalisé.





UNE PARTIE DU CODE À ÉTÉ RÉORGANISÉE À LA FIN ET IL EST DONC POSSIBLE QU'IL Y AIT DES ERREURS DANS LES CHEMINS, NOTAMMENT DANS LES CODES DE divers/ 

