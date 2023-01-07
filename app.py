import webbrowser
import pyautogui
from time import sleep

telefones = [555591056868, 555599732484, 555180463040]

# telefones = []
# with open('fones.txt', 'r') as arquivo:
#     telefones = [linha.replace('\n', '') for linha in arquivo]

# print(telefones)
primeiro_contato = True

for telefone in telefones:
    webbrowser.open(f'https://api.whatsapp.com/send?phone={telefone}')
    sleep(10)
    if primeiro_contato:
        # mensagem para whatsapp web clicar
        pyautogui.click(787, 221, duration=1)
        primeiro_contato = False
    else:
        pyautogui.click(678, 331, duration=1)
        sleep(2)
        pyautogui.click(795, 219, duration=1)
    sleep(10)
    pyautogui.click(793, 693, duration=1)
    pyautogui.typewrite('testando mensagem automatica de despedida da empresa')
    sleep(5)
    pyautogui.press('enter')
    sleep(10)
