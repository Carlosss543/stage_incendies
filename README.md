## Pour utilise le jeu de données

Pour créer le jeu de données final il faut lancer create_dataset_final.ipynb en spécifiant la valeur de split et de crop_size.
Il faut déjà avoir téléchargé le jeu de données data/dataset/split avec split égal à train, val ou test.

utils contient des fonctions auxiliaires et surtout un loader pytorch pour le jeu de données. Il y a un exemple d'utilisation de ce loader à l'emplacement divers/loader.ipynb.

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

#### Le dossier "create_datasets" contient des codes pour créer divers types de datasets qui m'ont été utiles au cours du projet.
**"create_attributs.ipynb" et "create_dataset_crops.ipynb" sont obsolètes car "create_dataset_final.ipynb" fait les deux et "create_datasets_crops_paires.ipynb" est seulement utile pour la partie segmentation. <br>**
- create_attributs.ipynb produit des paires (concepts, classes) <br>
- create_dataset_final.ipynb produit des triplets (images, concepts, classes) <br>
- create_datasets_crops_paires produit des paires (images, masques de brûlé) avec images pouvant être les images satellites ou annotées <br>
- create_datasets_crops.ipynb produit des paires (images, classes) avec images pouvant être les images satellites ou annotées

<br>

#### Le dossier "divers" contient des codes qui m'ont permis de faire des tests à différentes étapes ainsi que des codes pour obtenir des informations sur le dataset.
- training_curves contient les courbes d'entraînement associées aux poids se trouvant dans weight <br>
- loader.ipynb contient un exemple d'utilisation du loader associé au dataset final se trouvant dans utils <br>
- regression.ipynb entraîne une couche linéaire à prédire les classes à partir des attributs <br>
- resnet_sur_crops.ipynb entraîne un resnet18 à prédire la classe à partir d'un crop (d'image satellite ou d'image annotée) <br>
- resnet_sur_imgs.ipynb permet de faire la même chose avec des images de taille quelconque et pas nécessairement des crops <br>
- stats.ipynb contient des graphes et des statistiques sur les annotations des images et à permis de choisir ce qui était utile ou non pour la création des concepts <br>
- stats.txt contient un résumé de certaines de ces informations et **une explication de ce à quoi correpondent les différentes features** <br>
- tests.ipynb contient quelques tests faits sur le dataset (vérifier que les intersections des splits sont vides, trouver les tailles minimales et maximales des images)


<br>

#### Le dossier "interprétabilité" contient les différents modèles de l'architecture et des tests pour voir à quoi réagissent les neurones de la couche sparse du vae.
- training_curves contient les courbes d'entraînement associées aux poids se trouvant dans weight <br>
- interpretability.ipynb contient différents tests réalisés avec l'architecture finale (trouver les images qui activent un concept, trouver les images qui activent un neurone, trouver quels neurones contribuent à un concept et avec quel force et enfin des recherches de relations avec t-SNE)
- sparse_autoencoder.ipynb entraîne le sae à partir de l'avant dernière couche du resnet (les poids de ce derniers sont chargés depuis l'entraînement fait avec le code resnet_sur_imgs.ipynb du dossier divers)
- z_to_attributs.ipynb entraîne le fully_connected à relier les activations du sae aux concepts

<br>

#### Le dossier "approche_concurrente" contient l'implémentation d'une approche concurrente qui consiste à utiliser le Resnet18 pour prédire les attributs puis à utiliser une couche linéaire pour passer des attributs aux classes. Ainsi la prédiction des attributs ne se fait plus de manière implicite mais explicite.
- training_curves contient les courbes d'entraînement associées aux poids se trouvant dans weight <br>
- attributs_to_classes.ipynb entraîne une couche linéaire à prédire la classe à partir des concepts
- imgs_to_attributs.ipynb entraîne un resnet18 à prédire les concepts à partir de l'image satellite
- interpretabilite.ipynb n'est pas très complet, il contient seulement un code qui affiche les images activant le plus fortement un concept


#### Le dossier "segmentation_semantique" contient tous les codes de segmentation sémantique et de traitement d'images que j'ai réalisé.
- segmentation_semantique_ann.ipynb rajoute une conv transposed à un resnet18 pour prédire l'image annotée
- segmentation_semantique_atrous.ipynb fait quelque chose de similaire mais prédit le masque de brûlé et utilise des convolutions à trous
- segmentation_semantique_ouvertureSurfacique 1 et 2 pré traitent les masques de brûlé pour rendre la segmentation plus facile
- segmentation_semantique_pretrained.ipynb prédit le masque de brûlé en greffant une conv transposed à un resnet pré-entrainé pour prédire les classes
- segmentation_semantique_unet.ipynb prédit le masque de brûlé avec un unet
- traitement_images 1 et 2 étudies les transformations utilisées dans segmentation_semantique_ouvertureSurfacique

<br>

#### utils.py contient des fonctions qui sont réutilisées dans les autres parties du projet
- rajouter_features rajoute aux images annotées des nouvelles annotations correspondant aux intersections avec les masques de brûlé
- ImageDataset est le loader associé au dataset final
- random_90_rotation est une transformation pour faire de l'augmentation de données sur le jeu de données d'images satellites, cela fait tourner l'image de 0, 90, 180 ou 270 degré (invariances d'une image satellite)
- get_device renvoie le device disponible par ordre de priorité gpu puis mps (pour mac) puis cpu

<br>

## RÉCAPITULATIF DES ACCURACIES

| modèle    | train accuracy | val accuracy |
|-----------|----------------|--------------|
| Ligne 1   | Valeur A       | Valeur B     |
| Ligne 2   | Valeur C       | Valeur D     |

<br><br>

### NOTE : UNE PARTIE DU CODE À ÉTÉ RÉORGANISÉE À LA FIN ET IL EST DONC POSSIBLE QUE CERTAINS CHEMINS DOIVENT ÊTRE MODIFIÉS, NOTAMMENT DANS LES CODES DE divers/ 

