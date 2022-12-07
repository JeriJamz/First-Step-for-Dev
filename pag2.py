import pyautogui as pag


while True:
    pag.write('Hello World', interval = .25)
    pag.moveRel(10,10)
    pag.moveTo(500,500)
    pag.press('esc')
    break
