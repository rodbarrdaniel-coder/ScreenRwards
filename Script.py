import pyautogui as gui
import time
from pynput.keyboard import Controller, Key
import random
from questions import TotalSearchs


resolutions = ["", "1) 1366 x 768", "2) 1600 x 900", "3) 1920 x 1080", "4) 2560 x 1440", "5) 3840 x 2160",]

resolutionX = 0
resolutionY = 0

movemntTest = random.uniform(0,0)
movemntTest2 = random.uniform(0,0)


for resolutions in resolutions:
    print(resolutions)

msg = int(input("elige tu resolucion de pantalla: "))



if msg == 1:
    resolutionX = 1366
    resolutionY = 768

    
elif msg == 2:
   resolutionX = 1600
   resolutionY = 900



elif msg == 3:
   resolutionX = 1920
   resolutionY = 1080



elif msg == 4:
   resolutionX = 2560
   resolutionY = 1440



elif msg == 5:
   resolutionX = 3840
   resolutionY = 2160
else:
   totalResolutionsX = [1366,1600,1920,2560,3840] 
   totalResolutionsY = [768,900,1080,1440,2160] 
   resolutionX = random.choice(totalResolutionsX)
   resolutionY = random.choice(totalResolutionsY)
   print("resolucion random elegida")


   

print("resolucion", resolutionX, "x", resolutionY, "elejida")



movemntTest = resolutionX - 7
movemntTest2 = resolutionY/2
    

print("recuerda, si quieres detenerme solo presiona la tecla shift...")


#variable de pynput para controlar presione de teclas
tcl = Controller()

gui.PAUSE = 0
gui.MINIMUM_DURATION = 0
gui.MINIMUM_SLEEP = 0
gui.FAILSAFE = False


searchs = TotalSearchs
vuelta = 0

intentos = 0

intentRewards = 0
repo = "https://github.com/rodbarrdaniel-coder/ScreenRwards"

def movimientoRandom():
     duracion = random.uniform(0.4,1)
     coordX = random.uniform(0,resolutionX)
     coordY = random.uniform(0,resolutionY)
     gui.moveTo(coordX,coordY,duration=duracion,)
     time.sleep(0.4)

#funciones de tecleado

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




#este while puede ser mas rapido si quieres ya que estas fuera del  "modificalo a tu gusto"
while True:
    gui.press("win")
    time.sleep(0.2)
    gui.write("edge", interval=0.1)
    time.sleep(0.5)
    gui.press("enter")
    time.sleep(8)
    gui.press("f11")
    vuelta = 1
    if vuelta == 1:
        break


while True:
    movimientoRandom()
    print(resolutionX,resolutionY)
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
    gui.moveTo(movemntTest,movemntTest2, duration=0.7, tween=gui.easeInOutQuad)
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
      print("todo listo por hoy")
      break