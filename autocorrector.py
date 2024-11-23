import pyautogui
import pyperclip
import ollama
from win10toast import ToastNotifier

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
                'content': "Corrige uniquement les fautes d'orthographe, de grammaire et de ponctuation dans le texte ci-dessous sans ajouter de commentaires ni d'autres modifications :" + text,
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

autocorrector()
