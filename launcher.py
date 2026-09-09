import subprocess
import keyboard
import time


for i in range(5,0,-1):
    print("BOT ACTIVO EN: ",  i,  end="\r")
    time.sleep(1)

i = 0

if i == 0:
    proceso = subprocess.Popen(["python", "Script.py"])

    print("iniciado.")
    print("Pulsa SHIFT para detenerme.")

    keyboard.wait("shift")

    print("Deteniendo script...")
    proceso.terminate()