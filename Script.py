import pyautogui as gui
import time
from pynput.keyboard import Controller, Key
import random
from questions import TotalSearchs


#variable de pynput para controlar presione de teclas
tcl = Controller()

gui.PAUSE = 0
gui.MINIMUM_DURATION = 0
gui.MINIMUM_SLEEP = 0

searchs = TotalSearchs
vuelta = 0

intentos = 0

intentRewards = 0
repo = "https://github.com/rodbarrdaniel-coder/ScreenRwards"

#funciones de tecleado
def movimientoRandom():
     duracion = random.uniform(0.4,1)
     coordX = random.uniform(0,1366)
     coordY = random.uniform(0,1366)
     gui.moveTo(coordX,coordY,duration=duracion,)
     time.sleep(0.4)

def pressControl_T():
   tcl.press(Key.ctrl)
   tcl.press("t")
   time.sleep(0.1)
   tcl.release(Key.ctrl)
   tcl.release("t")
   time.sleep(0.1)

def presscontrol_tab():
   tcl.press(Key.ctrl)
   tcl.press(Key.tab)
   time.sleep(0.1)
   tcl.release(Key.ctrl)
   tcl.release(Key.tab)
   time.sleep(0.1)  

def presscontrol_w():
   tcl.press(Key.ctrl)
   tcl.press("w")
   time.sleep(0.5)
   tcl.release(Key.ctrl)
   tcl.release("w")
   time.sleep(0.5)

def presscontrol_l():
   tcl.press(Key.ctrl)
   tcl.press("l")
   time.sleep(0.5)
   tcl.release(Key.ctrl)
   tcl.release("l")
   time.sleep(0.5)   




def HumandsIntervals():
   intervalos = random.uniform(0.08,0.15)   
   return intervalos


movemntTest = random.uniform(237,683)
movemntTest2 = random.uniform(132,700)

#este while puede ser mas rapido si quieres ya que estas fuera del  "modificalo a tu gusto"
while True:
    gui.press("win")
    time.sleep(0.2)
    gui.write("edge", interval=0.01)
    time.sleep(0.1)
    gui.press("enter")
    time.sleep(8)
    gui.press("f11")
    vuelta = 1
    if vuelta == 1:
        break


while True:
    movimientoRandom()
    time.sleep(1)
    presscontrol_l()
    time.sleep(0.2)
    pregunta = random.choice(searchs)
    gui.press("delete")
    movimientoRandom()
    time.sleep(0.3)
    intervalGeneral = HumandsIntervals()

    for char in pregunta:
     tcl.type(char)
     time.sleep(intervalGeneral)  
    time.sleep(1.000)
    movimientoRandom() 

    gui.press("enter")

    time.sleep(2)
    gui.moveTo(1353,movemntTest2, duration=0.7, tween=gui.easeInOutQuad)
    gui.click()
    time.sleep(1)
    intentos += 1

    for i in range(1,10):
        gui.scroll(-105)
        time.sleep(0.7)
    time.sleep(2)

    for i in range(1,10):
     gui.scroll(105)
     time.sleep(0.7)

    time.sleep(1)
    movimientoRandom()
    time.sleep(0.2)
    movimientoRandom()
  

    if intentos >= 20:
     print("busquedas x escritura terminadas")
     time.sleep(1)
     intentos = 21
     time.sleep(0.5)
     break

time.sleep(3)

while intentos == 21:
   pressControl_T()
   time.sleep(0.5)
   presscontrol_tab()
   time.sleep(0.5) 
   presscontrol_w()
   time.sleep(0.5)
   presscontrol_l()

   for char in repo:
     tcl.type(char)
     time.sleep(HumandsIntervals())  
  
   time.sleep(1)
   gui.press("enter")

   intentRewards += 1

   if intentRewards == 1:
      print("todo listo")
      break