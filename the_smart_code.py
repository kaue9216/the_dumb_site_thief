import pyautogui
import time

pyautogui.PAUSE = 1

site = input('Digite o endereço do site que deseja copiar:')
name = input('Qual nome você dará a ele?')
# github.com

# time.sleep(5)

# print(pyautogui.position())

# abrir o terminal e criar a pasta do site
with pyautogui.hold('command'):
        pyautogui.press('space')

pyautogui.write("terminal")
pyautogui.press('enter')

pyautogui.write("cd")
pyautogui.press('enter')

pyautogui.write("cd code/kaue9216")
pyautogui.press('enter')

# pyautogui.write("mkdir smart_site")
# pyautogui.press('enter')
time.sleep(3)

# entrar no site e baixar o htlm
with pyautogui.hold('command'):
        pyautogui.press('space')

pyautogui.write("chrome")
pyautogui.press('enter')

with pyautogui.hold('command'):
        pyautogui.press('n')

pyautogui.write(site)
pyautogui.press('enter')

pyautogui.rightClick(x=157, y=511)
pyautogui.click(x=205, y=629)

pyautogui.write(name)
pyautogui.press('enter')

time.sleep(3)
pyautogui.click(x=1192, y=63)
pyautogui.click(x=1139, y=152)

#------------

time.sleep(5)

print(pyautogui.position())

with pyautogui.hold('command'):
        pyautogui.press('space')

pyautogui.write("ola mundo")



# renomear o arquivo html e mover para a pasta do site

# criar arquivo csv

# conectar o csv no html

# copiar o csv do site e colar no arquivo criado

# iniciar um servidor

# abrir o localhost

#------------

# time.sleep(5)

# print(pyautogui.position())

# with pyautogui.hold('command'):
#         pyautogui.press('space')

# pyautogui.write("ola mundo")
