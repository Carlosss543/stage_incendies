Pour créer le jeu de données final il faut lancer create_dataset_final.ipynb en changeant la valeur de split selon que l'on veut utiliser le "train", "val", ou "test".
Il faut déjà avoir le jeu de données data/dataset/split avec split égal à train, val ou test.



Les données sont dans le dossier data dont l'arborescence est :
    data
    ├─ dataset
    ├─ dataset_attributs
    ├─ dataset_crops
    ├─ dataset_crops_annotations
    ├─ dataset_crops_sat



create_dataset_crops.ipynb permet de créer des datasets de crop pour entraîner resnet_sur_crops.ipynb
create_attributs.ipynb permet de créer des datasets d'attributs pour entraîner regression.ipynb

