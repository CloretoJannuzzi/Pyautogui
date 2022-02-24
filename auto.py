import pyautogui
import time


pyautogui.alert('Código irá rodar, não mexa em nada até receber o alerta!')
pyautogui.PAUSE = 1.0

# abrir googledrive

pyautogui.press('win')
pyautogui.write('opera')
pyautogui.press('enter')
time.sleep(2)
pyautogui.write('https://drive.google.com/drive/u/0/my-drive')
pyautogui.press('enter')

# ir para area de trabalho

# neste código será jogado um arquivo para o drive
pyautogui.hotkey('win', 'm')
# usar o pyautgui.position() para descobrir a posição do mouse
# posicao onde o mouse deve pegar o arquivo, trocar x e y pelas coordenadas e remover as aspas
pyautogui.moveto('x, y')
pyautogui.mousedown()  # pressiona o botao esquerdo
# posicao onde o mouse deve soltar o arquivo, trocar x e y pelas coordenadas e remover as aspas
pyautogui.moveto('x, y')
pyautogui.hotkey('alt', 'tab')
pyautogui.mouseUp()  # onde quer soltar o arquivo

time.sleep(5)
pyautogui.alert('Código finalizado! Já pode voltar a utilizar o seu computador.')
