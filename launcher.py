import subprocess
import keyboard
import time


for i in range(5,0,-1):
    print("HI, vamos a elegir una resolucion de pantalla en: ",  i,  end="\r")
    time.sleep(0.9)

i = 0

if i == 0:
    proceso = subprocess.Popen(["python", "Script.py"])

    keyboard.wait("shift")
    
    print("Me he detenido 0w0")
    proceso.terminate()