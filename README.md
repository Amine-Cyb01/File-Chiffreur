# 🔐 File Chiffreur

Outil de chiffrement/déchiffrement de fichiers en AES-256 (CBC mode)

## Fonctionnalités
- Chiffrement AES-256 avec PBKDF2
- Gestion automatique du sel et IV
- Interface en ligne de commande

## Prérequis
- Python 3.6+
- pip

## Utilisation

## Chiffrement :

python src/file_cryptor.py encrypt -i test.txt -o encrypted.enc -p "motdepasse"

## Déchiffrement :

python src/file_cryptor.py decrypt -i encrypted.enc -o decrypted.txt -p "motdepasse"

## Sécurité

Utilisez des mots de passe complexes

Ne perdez jamais votre mot de passe

Le script est à but éducatif - audit sécurité recommandé pour usage professionnel

## Avertissement ⚠️

Le développeur n'est pas responsables des données perdues ou compromises.
