import requests
from bs4 import BeautifulSoup
import re
import pyautogui
import pyperclip
import time

cookies = {
    'gpt3': 'eee1b883-b713-45d8-9893-9b5c487674fd',
    '_ga_0CZ7G1YX87': 'GS1.1.1710153320.1.1.1710153369.11.0.0',
    '_ga': 'GA1.1.404669493.1710153320',
    'FCCDCF': '^%^5Bnull^%^2Cnull^%^2Cnull^%^2C^%^5B^%^22CP7Tt8AP7Tt8AEsACBFRArEoAP_gAEPgACIgINJD7D7FbSFCwHpzaLsAMAhHRsCAQoQAAASBAmABQAKQIAQCgkAQFASgBAACAAAAICZBIQAECAAACUAAQAAAAAAEAAAAAAAIIAAAgAEAAAAIAAACAAAAEAAIAAAAEAAAmAgAAIIACAAAhAAAAAAAAAAAAAAAAgAAAAAAAAAAAAAAAAAAAQOhQD2F2K2kKFkPCmQWYAQBCijYEAhQAAAAkCBIAAgAUgQAgFIIAgAIFAAAAAAAAAQEgCQAAQABAAAIACgAAAAAAIAAAAAAAQQAAAAAIAAAAAAAAEAAAAAAAQAAAAIAABEhCAAQQAEAAAAAAAQAAAAAAAAAAABAAA^%^22^%^2C^%^222~2072.70.89.93.108.122.149.196.2253.2299.259.2357.311.313.323.2373.338.358.2415.415.449.2506.2526.486.494.495.2568.2571.2575.540.574.2624.609.2677.864.981.1029.1048.1051.1095.1097.1126.1205.1211.1276.1301.1344.1365.1415.1423.1449.1451.1570.1577.1598.1651.1716.1735.1753.1765.1870.1878.1889.1958~dv.^%^22^%^2C^%^229519E7A8-4ABF-45D2-86E5-CD71A0B8273F^%^22^%^5D^%^5D',
    '__gads': 'ID=7eb247334b849f97:T=1710153323:RT=1710153323:S=ALNI_Ma2tuNuGoKd-p3YeHg7EEvfoMed-w',
    '__gpi': 'UID=00000d425c7faa8e:T=1710153323:RT=1710153323:S=ALNI_MYsapHBVZN35jNapgJHQF1c8AEebw',
    '__eoi': 'ID=9a3adf76d245482b:T=1710153323:RT=1710153323:S=AA-AfjZ7OIZ7XxEi_EE8qwiJKo3l',
    'FCNEC': '^%^5B^%^5B^%^22AKsRol_vzfQ2lI_1lqVUe0uPlVD-sNWZEOQylV1PdMyjfQZSIodJ8r9ITKUrbu-YtI8P7XuQOhpXz1Zn7PyaqFL_crPnsEKGRoeRYvyC5n8NNRnUy0iW2FtN9T3IXAzVhmOYUTzamp7XnJggRKMWEfzOYRcKnjGjnw^%^3D^%^3D^%^22^%^5D^%^5D',
}

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:124.0) Gecko/20100101 Firefox/124.0',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
    'Accept-Language': 'fr,fr-FR;q=0.8,en-US;q=0.5,en;q=0.3',
    # 'Accept-Encoding': 'gzip, deflate, br',
    'Content-Type': 'application/x-www-form-urlencoded',
    'Origin': 'https://ile-reunion.org',
    'Connection': 'keep-alive',
    'Referer': 'https://ile-reunion.org/gpt3/',
    # 'Cookie': 'gpt3=eee1b883-b713-45d8-9893-9b5c487674fd; _ga_0CZ7G1YX87=GS1.1.1710153320.1.1.1710153369.11.0.0; _ga=GA1.1.404669493.1710153320; FCCDCF=^%^5Bnull^%^2Cnull^%^2Cnull^%^2C^%^5B^%^22CP7Tt8AP7Tt8AEsACBFRArEoAP_gAEPgACIgINJD7D7FbSFCwHpzaLsAMAhHRsCAQoQAAASBAmABQAKQIAQCgkAQFASgBAACAAAAICZBIQAECAAACUAAQAAAAAAEAAAAAAAIIAAAgAEAAAAIAAACAAAAEAAIAAAAEAAAmAgAAIIACAAAhAAAAAAAAAAAAAAAAgAAAAAAAAAAAAAAAAAAAQOhQD2F2K2kKFkPCmQWYAQBCijYEAhQAAAAkCBIAAgAUgQAgFIIAgAIFAAAAAAAAAQEgCQAAQABAAAIACgAAAAAAIAAAAAAAQQAAAAAIAAAAAAAAEAAAAAAAQAAAAIAABEhCAAQQAEAAAAAAAQAAAAAAAAAAABAAA^%^22^%^2C^%^222~2072.70.89.93.108.122.149.196.2253.2299.259.2357.311.313.323.2373.338.358.2415.415.449.2506.2526.486.494.495.2568.2571.2575.540.574.2624.609.2677.864.981.1029.1048.1051.1095.1097.1126.1205.1211.1276.1301.1344.1365.1415.1423.1449.1451.1570.1577.1598.1651.1716.1735.1753.1765.1870.1878.1889.1958~dv.^%^22^%^2C^%^229519E7A8-4ABF-45D2-86E5-CD71A0B8273F^%^22^%^5D^%^5D',
    'Upgrade-Insecure-Requests': '1',
    'Sec-Fetch-Dest': 'document',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-Site': 'same-origin',
    'Sec-Fetch-User': '?1',
    # Requests doesn't support trailers
    # 'TE': 'trailers',
}

class config:
    ctrlc = ""

def transform_texte(texte):
    texte_transform = ""
    for caractere in texte:
        if caractere == " ":
            texte_transform += "+"
        elif caractere.isalnum():
            texte_transform += caractere
        else:
            texte_transform += "^%" + "^".join([hex(ord(c)).replace('0x', '').upper() for c in caractere])
    return texte_transform




def autocorrector():
    transform_texte(config.ctrlc)
    time.sleep(2)
    pyautogui.hotkey('ctrl', 'a')
    pyautogui.hotkey('ctrl', 'c')
    pyautogui.press('backspace')
    pyautogui.write("Correction en cours...")
    config.ctrlc = pyperclip.paste()
    data = f'D1=Option+sortie+audio&xscreen=1920&yscreen=1080&question=Tu+dois+juste+donner+la+r^%^C3^%^A9ponse^%^2C+corrige+les+fautes+{config.ctrlc}'
    response = requests.post('https://ile-reunion.org/gpt3/resultat', cookies=cookies, headers=headers, data=data)
    # Analyser le contenu de la réponse avec BeautifulSoup
    soup = BeautifulSoup(response.text, 'html.parser')
    # Trouver l'élément contenant le texte souhaité
    resultat_div = soup.find('div', class_='affichage')
    # Extraire le texte à partir de cet élément
    texte = resultat_div.get_text(strip=True)
    # Retirer les parties indésirables du texte
    texte = texte.replace('Résultat : gpt-3.5-turbo', '')
    texte = re.sub(r'Posez une autre question.*', '', texte)
    # Imprimer le texte extrait
    print(texte)
    pyautogui.hotkey('ctrl', 'a')
    pyautogui.hotkey('ctrl', 'c')
    pyautogui.press('backspace')
    pyperclip.copy(texte)
    pyautogui.hotkey('ctrl', 'v')

autocorrector()
