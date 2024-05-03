import requests
import pyautogui
import pyperclip
import time

def autocorrector():
    pyautogui.hotkey('ctrl', 'c')
    pyautogui.press('backspace')
    text = pyperclip.paste()
    text = text.replace("'", "\\'")
    headers = {
        'accept': '*/*',
        'accept-language': 'fr-FR,fr;q=0.9,en-US;q=0.8,en;q=0.7',
        'content-type': 'text/plain;charset=UTF-8',
        'dnt': '1',
        'origin': 'https://www.llama2.ai',
        'priority': 'u=1, i',
        'referer': 'https://www.llama2.ai/',
        'sec-ch-ua': '"Not-A.Brand";v="99", "Chromium";v="124"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36',
    }

    data = {
        "prompt": f"system\nYou are a helpful assistant.\nuser\n\nTu est un correcteur d'orthographe, je vais te donner une phrase que tu va devoir corriger mais attention tu dois UNIQUEMENT répondre par ça: {text}\n",
        "model": "meta/meta-llama-3-70b-instruct",
        "systemPrompt": "You are a helpful assistant.",
        "temperature": 0.75,
        "topP": 0.9,
        "maxTokens": 800,
        "image": None,
        "audio": None
    }

    response = requests.post('https://www.llama2.ai/api', headers=headers, json=data)
    pyperclip.copy(response.text)
    pyautogui.hotkey('ctrl', 'v')

autocorrector()