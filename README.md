# ScreenRwards v0.1.0-alpha

Automatización en Python para la ejecución de búsquedas automáticas y la acumulación de puntos diarios en Microsoft Rewards.

A diferencia de otros métodos de automatización, como el **web scraping** o determinadas extensiones de navegador, ScreenRwards interactúa directamente con la interfaz gráfica mediante **teclado y ratón**, buscando que las acciones se asemejen más a una interacción manual.

El proyecto incorpora pausas variables, movimientos e intervalos de escritura para evitar que todas las acciones se ejecuten exactamente de la misma manera.

> ⚠️ **Importante:** ninguna técnica de automatización puede garantizar que una cuenta no sea detectada o sancionada. El objetivo de este proyecto es **reducir el riesgo asociado a una automatización demasiado predecible**, no garantizar la ausencia de detección.

---

## ✨ Características

* **🖱️ Control del ratón:** interacción con la interfaz gráfica mediante `pyautogui`.

* **⌨️ Control del teclado:** simulación de pulsaciones mediante `pynput`.

* **⏱️ Tiempos variables:** pausas aleatorias entre diferentes acciones.

* **✍️ Velocidad de escritura variable:** diferentes intervalos entre pulsaciones para evitar una cadencia completamente constante.

* **🖥️ Interacción con la interfaz:** las acciones se realizan sobre la interfaz gráfica del navegador en lugar de realizar solicitudes HTTP directamente.

* **🔄 Automatización de tareas repetitivas:** permite automatizar las búsquedas diarias.

* **❤ +34k de preguntas random**.

---

## 🛡️ Enfoque de automatización

Uno de los objetivos principales de ScreenRwards es utilizar un método de automatización que se acerque más a la forma en la que una persona interactúa normalmente con un ordenador.

En lugar de utilizar técnicas como:

* Web scraping directo.
* Solicitudes HTTP automatizadas.
* Manipulación directa de páginas mediante APIs.
* Automatización basada exclusivamente en el DOM.
* Extensiones específicas para automatizar las búsquedas.

ScreenRwards utiliza la **interfaz gráfica del sistema operativo**, realizando acciones como:

* Mover el ratón.
* Hacer clic.
* Escribir mediante el teclado.
* Esperar diferentes intervalos de tiempo.
* Interactuar con el navegador de forma similar a un usuario.

Además, el programa introduce cierta variabilidad en los tiempos de espera y en la velocidad de escritura para evitar que todas las ejecuciones sigan exactamente el mismo patrón.

> **Nota:** este enfoque busca reducir la previsibilidad de la automatización, pero no significa que las acciones sean indistinguibles de las realizadas por una persona ni que estén exentas de detección.

---

## 💡 Consejos de uso

### Estado del proyecto

Actualmente, el proyecto está disponible como código fuente de Python.

Próximamente se pretende publicar una versión ejecutable `.exe` para facilitar su utilización en Windows sin necesidad de instalar Python ni configurar manualmente el entorno.

### Requisitos previos

Se recomienda tener conocimientos básicos sobre:

* Python.
* Entornos virtuales.
* Uso de la terminal.
* Instalación de dependencias mediante `pip`.

> 💡 **Consejo:** antes de iniciar el programa, asegúrate de tener Microsoft Edge instalado y haber iniciado sesión con tu cuenta de Microsoft.

---

## ⚠️ Advertencia y disclaimer

**El uso de este script es responsabilidad del usuario.**

ScreenRwards es una herramienta de automatización y, como cualquier herramienta de este tipo, puede entrar en conflicto con las políticas o condiciones de determinados servicios.

El proyecto intenta utilizar interacciones a través de teclado, ratón e interfaz gráfica en lugar de realizar scraping o solicitudes automatizadas directamente. Esto puede hacer que el comportamiento sea **menos predecible comparado con extensiones de navegador o otras formas de automatización**, pero no garantiza que Microsoft no pueda identificarlo como una actividad automatizada.

El uso de esta herramienta podría provocar:

* Restricciones temporales de la cuenta.
* Suspensión o pérdida del acceso al programa Microsoft Rewards.
* Pérdida de los puntos acumulados.
* Otras medidas aplicadas de acuerdo con las políticas de Microsoft.

Este proyecto ha sido creado principalmente con **fines educativos y de aprendizaje**, especialmente para experimentar con Python, automatización de interfaces gráficas y control de dispositivos de entrada "no me hago responsable de cualquier baneo".

El desarrollador no se hace responsable de las consecuencias derivadas del uso de este software.

---

## ⚖️ Ventajas y desventajas

### ✅ Ventajas

1. **Interacción mediante interfaz gráfica:** utiliza teclado y ratón en lugar de depender exclusivamente de scraping o solicitudes directas.
2. **Mayor variabilidad:** incorpora pausas y velocidades de escritura variables.
3. **Automatización sencilla:** permite automatizar tareas repetitivas.
4. **Proyecto ligero:** no requiere conocimientos avanzados para comenzar a utilizarlo.
5. **Enfoque educativo:** permite aprender sobre automatización, Python y control de interfaces gráficas.

### ❌ Desventajas

1. **El ordenador queda ocupado:** mientras se ejecuta la automatización, puede resultar difícil utilizar el equipo con normalidad.
2. **Dependencia de la interfaz:** los cambios en Microsoft Edge o Microsoft Rewards pueden hacer que el programa deje de funcionar correctamente.
3. **Dependencia de la resolución:** algunas acciones utilizan posiciones concretas del ratón.
4. **Compatibilidad limitada:** actualmente está pensado principalmente para Windows.
5. **No elimina el riesgo de detección:** sigue siendo una herramienta automatizada.

---

## 🛠️ Requisitos e instalación

### 1. Clonar el repositorio

Clona el repositorio y accede a la carpeta del proyecto:

```powershell
git clone https://github.com/rodbarrdaniel-coder/ScreenRwards.git
cd ScreenRwards
```


### 2. Crear el entorno virtual

Se recomienda utilizar un entorno virtual para mantener las dependencias del proyecto aisladas del resto de instalaciones de Python.

```powershell
python -m venv .venv
```

### 3. Activar el entorno virtual

En PowerShell:

```powershell
.venv\Scripts\Activate.ps1
```

Si se ha activado correctamente, aparecerá `(.venv)` al principio de la línea de comandos:

```text
(.venv) PS D:\WORK_SPACE\ScreenRwards>
```

### 4. Instalar las dependencias

Con el entorno virtual activado:

```powershell
python -m pip install pyautogui pynput pillow
```

#### Dependencias utilizadas

| Librería    | Uso                                                                              |
| ----------- | ------------------------------------------------------------------------------   |
| `pyautogui` | Control del ratón, teclado e interacción con la interfaz gráfica.                |
| `pynput`    | Control y simulación de eventos de teclado.                                      |
| `Pillow`    | Procesamiento de imágenes y pixeles funciones de `pyautogui` "NO OBLIGATORIO".   |
| `time`      | Control de tiempos y pausas.                                                     |
| `random`    | Generación de valores aleatorios.                                                |

> `time` y `random` forman parte de la biblioteca estándar de Python, por lo que no es necesario instalarlas mediante `pip`.

### 5. Ejecutar el proyecto

Con el entorno virtual activado:

```powershell
python main.py
```

---

## 📁 Estructura del proyecto

```text
ScreenRwards/
│
├── .venv/              # Entorno virtual
├── script.py          # Funciones relacionadas con Rewards
├── questions.py        # Funciones relacionadas con búsquedas/preguntas
├── README.md           # Documentación
└── LICENSE             # Licencia del proyecto
```

---

## 📄 Licencia

Este proyecto está publicado bajo la licencia **MIT**.

Consulta el archivo [`LICENSE`](LICENSE) para conocer los términos completos de la licencia.

Eres libre de utilizar, modificar y distribuir este código de acuerdo con las condiciones establecidas por la licencia MIT.

---

## 🚀 Próximas actualizaciones

* [ ] Publicar una versión ejecutable `.exe`.
* [ ] Mejorar la compatibilidad con diferentes resoluciones de pantalla.
* [ ] Mejorar la gestión de errores.
* [ ] Reducir la dependencia de coordenadas fijas.
* [ ] Mejorar la compatibilidad con diferentes configuraciones de Windows.
* [ ] Añadir un sistema de configuración más sencillo.
* [ ] Mejorar la estabilidad de la automatización.
* [ ] Mejorar la movilidad del mouse.

---

## 📝 Nota del desarrollador

Este es mi **primer repositorio público** y forma parte de mi proceso de aprendizaje y mejora constante en Python y desarrollo de software.

Por este motivo, pueden existir errores, problemas de compatibilidad o partes del código que todavía puedan mejorarse.

Cualquier sugerencia o comentario constructivo es bienvenido. 🙂

por sierto lo probe en gatcha y efectivamente pasa los estandares de no soy un robot

## Mi experiencia

El proyecto lleva de 2 a 4 semanas de uso personal, lo que me ha permitido ir realizando ajustes y mejoras en el sistema de automatización y hasta el momento sigue funcionando.

Aun así, los resultados pueden variar dependiendo de factores como la configuración del equipo, resolución de pantalla, navegador y cambios realizados en Microsoft Rewards.

### ⚠️ Compatibilidad con la resolución

El proyecto fue desarrollado inicialmente en un portátil con una resolución de **1366 × 768 píxeles**.

Debido a que algunas acciones utilizan posiciones concretas del ratón, pueden producirse errores al utilizar el programa con otras resoluciones, escalas de pantalla o configuraciones diferentes.

Este es uno de los aspectos que se pretende mejorar en futuras versiones.

---

**ScreenRwards v0.1.0-alpha**

Proyecto desarrollado como parte de un proceso de aprendizaje en Python.
