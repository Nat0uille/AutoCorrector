import webbrowser
import pyautogui
import pyperclip
import ollama
from win10toast import ToastNotifier
import pystray
from PIL import Image, ImageDraw
import threading
import keyboard

toaster = ToastNotifier()

def autocorrector():
    pyautogui.hotkey('ctrl', 'c')
    pyautogui.press('backspace')
    text = pyperclip.paste()
    text = text.replace("'", "\\'")
    try:
        response = ollama.chat(model='llama3.2', messages=[
            {
                'role': 'user',
                'content': "Corrige uniquement les fautes dans le texte ci-dessous. Fournis exclusivement la version corrigée, sans ajout de commentaires, d'introduction ou de contexte. Voici le texte :" + text,
            },
        ])
        if 'message' in response and 'content' in response['message']:
            corrected_text = response['message']['content']
        else:
            toaster.show_toast(
                "Auto Corrector",
                "Erreur: La réponse de l'API ne contient pas les clés attendues.",
                duration=10,
                icon_path=None
                )
            return
    except Exception as e:
        toaster.show_toast(
            "Auto Corrector",
            f"Erreur lors de l'appel à l'API: {e}",
            duration=10,
            icon_path=None
            )
        return
    pyperclip.copy(corrected_text)
    pyautogui.hotkey('ctrl', 'v')

def create_image():
    image = Image.open("logo.png")
    return image

def on_quit(icon, item):
    icon.stop()
    global running
    running = False

def setup(icon):
    icon.visible = True

icon = pystray.Icon("AutoCorrector")
icon.icon = create_image()
icon.menu = pystray.Menu(
    pystray.MenuItem("AutoCorrector v2.5", None, enabled=False),
    pystray.MenuItem("Par Nat0uille", None, enabled=False),
    pystray.MenuItem("Ajouter-nous une étoile sur Github !", lambda: webbrowser.open("https://github.com/Nat0uille/AutoCorrector")),
    pystray.MenuItem("Quitter", on_quit)
)

if __name__ == "__main__":
    running = True
    thread = threading.Thread(target=icon.run, daemon=True)
    thread.start()
    keyboard.add_hotkey('F23', autocorrector)
    
    while running:
        keyboard.wait('F23')