import pyautogui
import pyperclip
import ollama

def autocorrector():
    pyautogui.hotkey('ctrl', 'c')
    pyautogui.press('backspace')
    text = pyperclip.paste()
    text = text.replace("'", "\\'")
    try:
        response = ollama.chat(model='llama3.1', messages=[
            {
                'role': 'user',
                'content': "Corrige uniquement les fautes d'orthographe, de grammaire et de ponctuation dans le texte ci-dessous sans ajouter de commentaires ni d'autres modifications :" + text,
            },
        ])
        if 'message' in response and 'content' in response['message']:
            corrected_text = response['message']['content']
        else:
            print("Erreur: La réponse de l'API ne contient pas les clés attendues.")
            return
    except Exception as e:
        print(f"Erreur lors de l'appel à l'API: {e}")
        return
    print(corrected_text)
    pyperclip.copy(corrected_text)
    pyautogui.hotkey('ctrl', 'v')

autocorrector()
