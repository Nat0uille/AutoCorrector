# ✒️Autocorrector

`Autocorrector` est un script Python qui utilise une API de traitement du langage naturel pour corriger automatiquement les fautes d'orthographe, de grammaire et de ponctuation dans un texte copié. Le texte corrigé est ensuite automatiquement collé à l'emplacement d'origine.

## Prérequis

Avant de pouvoir utiliser ce script, assurez-vous d'avoir installé les bibliothèques Python nécessaires :

- `pyautogui`
- `pyperclip`
- `ollama`

Vous pouvez les installer en utilisant `pip` :

```sh
pip install pyautogui pyperclip ollama
```
Et vous devez aussi installer `llama3.1` :
```sh
ollama run llama3.1
```
## Utilisation

1. **Copiez le texte** que vous souhaitez corriger.
2. **Exécutez le script** `autocorrector.py`.
3. Le texte corrigé sera automatiquement collé à l'emplacement d'origine.

## Fonctionnement

1. Le script utilise `pyautogui` pour copier le texte sélectionné (avec `ctrl + c`).
2. Le texte copié est récupéré à l'aide de `pyperclip`.
3. Le texte est envoyé à l'API `ollama` pour correction.
4. Le texte corrigé est récupéré et copié dans le presse-papier.
5. Le texte corrigé est collé à l'emplacement d'origine (avec `ctrl + v`).

## Remarques

- Assurez-vous d'avoir `ollama` sur votre ordinateur et de lancé avec le model `llama3.1`.
- Personnellement je l'utilise avec mon streamdeck avec [Auto PY to EXE](https://pypi.org/project/auto-py-to-exe/)
- Ce script est conçu pour fonctionner sous Windows avec les raccourcis clavier `ctrl + c` et `ctrl + v`. Vous devrez peut-être ajuster les raccourcis si vous utilisez un autre système d'exploitation.

## Contribuer

Les contributions sont les bienvenues ! Pour signaler des problèmes ou proposer des améliorations, veuillez ouvrir une issue ou soumettre une pull request sur le dépôt GitHub du projet.

## Licence

Ce projet est sous licence MIT. Voir le fichier [LICENSE](LICENSE) pour plus de détails.
