import pyautogui
import time

pyautogui.PAUSE = 1

# site = input('Digite o endereço do site que deseja copiar:')
# name = input('Qual nome você dará a ele?')
# github.com

# time.sleep(5)

# print(pyautogui.position())

# abrir o terminal e criar a pasta do site
with pyautogui.hold('command'):
        pyautogui.press('space')

pyautogui.write("terminal")
pyautogui.press('enter')

time.sleep(1)
pyautogui.write("cd")
pyautogui.press('enter')

pyautogui.write("cd code/kaue9216")
pyautogui.press('enter')

pyautogui.write("mkdir smart_site")
pyautogui.press('enter')
# time.sleep(3)

pyautogui.write("cd smart_site")
pyautogui.press('enter')

# entrar no site e baixar o htlm
with pyautogui.hold('command'):
        pyautogui.press('space')

pyautogui.write("chrome")
pyautogui.press('enter')

with pyautogui.hold('command'):
        pyautogui.press('n')

# pyautogui.write(site)
pyautogui.write("github.com")
pyautogui.press('enter')

pyautogui.rightClick(x=157, y=511)
pyautogui.click(x=205, y=629)

# pyautogui.write(name)
pyautogui.write("github2")
pyautogui.press('enter')

time.sleep(3)
pyautogui.click(x=1192, y=63)
pyautogui.click(x=1139, y=152)

with pyautogui.hold('fn'):
    pyautogui.press('f')
# renomear o arquivo html e mover para a pasta do site

pyautogui.rightClick(x=299, y=97)
pyautogui.click(x=338, y=339)

with pyautogui.hold('command'):
        pyautogui.press('f')

pyautogui.write("smart_site")
pyautogui.press('enter')

pyautogui.rightClick(x=266, y=175)
pyautogui.click(x=288, y=182)
pyautogui.rightClick(x=288, y=182)
pyautogui.click(x=331, y=215)

with pyautogui.hold('command'):
        pyautogui.press('space')

pyautogui.write("terminal")
pyautogui.press('enter')

pyautogui.write("code .")
pyautogui.press('enter')
time.sleep(3)

# criar arquivo css
pyautogui.click(x=123, y=127)

pyautogui.write("sty.css")
pyautogui.press('enter')

with pyautogui.hold('command'):
        pyautogui.press('space')

# copiar o css do site e colar no arquivo criado
pyautogui.write("chrome")
pyautogui.press('enter')
pyautogui.rightClick(x=157, y=511)
pyautogui.click(x=193, y=867)
time.sleep(3)

# selecionar o texto do css
pyautogui.moveTo(1120, 225)
pyautogui.mouseDown(button='left')
pyautogui.moveTo(1350, 896, duration=2)
time.sleep(195)
pyautogui.mouseUp(button='left')

with pyautogui.hold('command'):
        pyautogui.press('c')

with pyautogui.hold('command'):
        pyautogui.press('space')

pyautogui.write("visual studio code")
pyautogui.press('enter')

pyautogui.click(x=737, y=609)

with pyautogui.hold('command'):
        pyautogui.press('v')

time.sleep(5)

pyautogui.click(x=121, y=175)
time.sleep(1)
pyautogui.click(x=737, y=609)

# conectar o css no html
# o python não consegue escrever html, resolver isso
pyautogui.write('link')
pyautogui.press('tab')
pyautogui.write("sty.css")

pyautogui.click(x=743, y=862)

# iniciar um servidor
pyautogui.write("serve")
pyautogui.press('enter')

with pyautogui.hold('command'):
        pyautogui.press('space')

pyautogui.write("chrome")
pyautogui.press('enter')

with pyautogui.hold('command'):
        pyautogui.press('t')

# abrir o localhost
pyautogui.write("localhost:8000")
pyautogui.press('enter')

pyautogui.click(x=70, y=204)
time.sleep(5)

with pyautogui.hold('command'):
        pyautogui.press('t')

pyautogui.write("how can I fix CSS")
pyautogui.press('enter')


## ------------

time.sleep(5)

# print(pyautogui.position())

with pyautogui.hold('command'):
        pyautogui.press('space')

pyautogui.write("ola mundo")
