# ✒️Autocorrector

`Autocorrector` est un script Python qui utilise une API de traitement du langage naturel pour corriger automatiquement les fautes d'orthographe, de grammaire et de ponctuation dans un texte copié. Le texte corrigé est ensuite automatiquement collé à l'emplacement d'origine.

## Prérequis

Avant de pouvoir utiliser ce script, assurez-vous d'avoir installé les bibliothèques Python nécessaires :

- `pyautogui`
- `pyperclip`
- `ollama`
- `win10toast`
- `pystray`
- `PIL` (Pillow)
- `keyboard`

Vous pouvez les installer en utilisant `pip` :

```sh
pip install pyautogui pyperclip ollama win10toast pystray pillow keyboard
```
Et vous devez aussi installer `llama3.2` :
```sh
ollama run llama3.2
```
## Utilisation

1. **Lancer le fichier python** (si vous voulez ne pas avoir le terminal d'affiché, changer .pyw à la place de .py)
2. **Appuyer sur la touche défini** (F23 de base)

## Remarques

- Assurez-vous d'avoir `ollama` sur votre ordinateur et de lancé avec le model `llama3.2`.
- Ce script est conçu pour fonctionner sous Windows 11 avec les raccourcis clavier `ctrl + c` et `ctrl + v`. Vous devrez peut-être ajuster les raccourcis si vous utilisez un autre système d'exploitation.

## Licence

Ce projet est sous licence MIT. Voir le fichier [LICENSE](LICENSE) pour plus de détails.
