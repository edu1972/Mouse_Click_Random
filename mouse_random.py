import pyautogui
import random

# Obtém as dimensões da tela
largura, altura = pyautogui.size()

try:
    while True:
        # Gera coordenadas aleatórias dentro da área da tela
        x = random.randint(0, largura)
        y = random.randint(0, altura)

        # Move o mouse para as coordenadas geradas
        pyautogui.moveTo(x, y, duration=0.5)

        # Simula um clique do mouse
        pyautogui.click()

except KeyboardInterrupt:
    # Interrompe o programa quando pressionar Ctrl + C
    pass
