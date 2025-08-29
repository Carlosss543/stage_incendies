### Pour utilise le jeu de données

Pour créer le jeu de données final il faut lancer create_dataset_final.ipynb en spécifiant la valeur de split et de crop_size.
Il faut déjà avoir téléchargé le jeu de données data/dataset/split avec split égal à train, val ou test.

utils contient des fonctions auxiliaires et surtout un loader pytorch pour le jeu de donné. Il y a un exemple d'utilisation de ce loader à l'emplacement divers/loader.ipynb.

<br>

---

<br>

## Descriptif détaillé par dossier


Les données sont dans le dossier data dont l'arborescence est : <br>
    data <br>
    ├─ dataset <br>
    ├─ dataset_attributs <br>
    ├─ dataset_crops <br>
    ├─ dataset_crops_annotations <br>
    ├─ dataset_crops_paires <br>
    ├─ dataset_crops_satv

<br>

#### Le dossier "create_datasets" contient des codes pour créer divers types de datasets qui m'ont été utiles au cours de ce projet.<br>"create_attributs.ipynb" et "create_dataset_crops.ipynb" sont obsolètes car "create_dataset_final.ipynb" fait les deux et "create_datasets_crops_paires.ipynb" est seulement utile pour la partie segmentation. <br>
-create_attributs.ipynb produit des paires (concepts, classes) <br>
-create_dataset_final.ipynb produit des triplets (images, concepts, classes) <br>
-create_datasets_crops_paires produit des paires (images, masques de brûlé) avec images pouvant être les images satellites ou annotées <br>
-create_datasets_crops.ipynb produit des paires (images, classes) avec images pouvant être les images satellites ou annotées

<br>

##### Le dossier "divers" contient des codes qui m'ont permis de faire des tests à différentes étapes ainsi que des codes pour obtenir des informations sur le dataset.
    training_curves contient les courbes d'entraînement associées aux poids se trouvant dans weight
    loader.ipynb contient un exemple d'utilisation du loader associé au dataset final se trouvant dans utils
    regression.ipynb entraîne une couche linéaire à prédire les classes à partir des attributs
    resnet_sur_crops.ipynb entraîne un resnet18 à prédire la classe à partir d'un crop (d'image satellite ou d'image annotée)
    resnet_sur_imgs.ipynb permet de faire la même chose avec des images de taille quelconque et pas nécessairement des crops
    stats.ipynb contient des graphes et des statistiques sur les annotations des images et à permis de choisir ce qui était utile ou non pour la création des concepts
    stats.txt contient un résumé de certaines de ces informations et **une explication de ce à quoi correpondent les différentes features**
    tests.ipynb contient quelques tests faits sur le dataset (vérifier que les intersections des splits sont vides, trouver les tailles minimales et maximales des images)


<br><br>

#### Le dossier "interprétabilité" contient les différents modèles de l'architecture et des tests pour voir à quoi réagissent les neurones de la couche sparse du vae.

Le dossier "approche_concurrente" contient l'implémentation d'une approche concurrente qui consiste à utiliser le Resnet18 pour prédire les attributs puis à utiliser une couche linéaire pour passer des attributs aux classes. Ainsi la prédiction des attributs ne se fait plus de manière implicite mais explicite.

Le dossier "segmentation_semantique" contient tous les codes de segmentation sémantique et de traitement d'images que j'ai réalisé.





UNE PARTIE DU CODE À ÉTÉ RÉORGANISÉE À LA FIN ET IL EST DONC POSSIBLE QU'IL Y AIT DES ERREURS DANS LES CHEMINS, NOTAMMENT DANS LES CODES DE divers/ 

