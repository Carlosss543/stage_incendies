Pour créer le jeu de données final il faut lancer create_dataset_final.ipynb en changeant la valeur de split selon que l'on veut utiliser le "train", "val", ou "test".
Il faut déjà avoir téléchargé le jeu de données data/dataset/split avec split égal à train, val ou test.


Il y a un exemple de loader pytorch dans loader.ipynb.



Les données sont dans le dossier data dont l'arborescence est :
    data
    ├─ dataset
    ├─ dataset_crops
    <!-- ├─ dataset_attributs
    ├─ dataset_crops_annotations
    ├─ dataset_crops_sat -->







Le dossier "approche_concurrente" contient comme son nom l'indique l'implémentation d'une approche concurrente qui consiste à utiliser le Resnet18 pour prédire les attributs puis à utiliser une couche linéaire pour passer des attributs aux classes. Ainsi la prédiction des attributs ne se fait plus de manière implicite mais explicite.

