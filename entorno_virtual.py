**ENTORNO VIRTUAL EN PYTHON**

**¿QUÉ ES UN ENTORNO VIRTUAL EN PYTHON?**

Un entorno virtual en Python es un entorno aislado que te permite tener una instalación independiente de Python con sus propios paquetes y dependencias, sin afectar al resto del sistema ni a otros proyectos.

En otras palabras, es como una “burbuja” donde puedes instalar librerías específicas para un proyecto sin interferir con otros proyectos o con la instalación global de Python.


**¿CÓMO CREAR EL ENTORNO VRTUAL?**

En la consola ejecutar:

        python -m venv nombre_del_entorno

Para activar el entorno virtual se ejecuta el siguiente comando:

		nombre_del_entorno\Scripts\activate

Cuando se activa, verás el nombre del entorno al inicio de la línea de comandos, por ejemplo:

		(nombre_del_entorno) $


**¿CÓMO INSTALAR PAQUETES DENTRO DEL ENTORNO?**

Una vez activado:

		pip install nombre_del_paquete

También se pueden descargar varias dependencias a la vez, ejemplo:	
 
		pip install numpy pandas matplotlib


*Para desactivar el entorno virtual:*

		deactivate

**RECREAR EL MISMO ENTORNO EN OTRO LUGAR**

		pip install -r requirements.txt


**COMANDOS DE PAQUETES-DEPENDENCIAS**

Guardar dependencias

		pip freeze > requirements.txt


Ver qué paquetes tienes instalados:

		pip list

Actualizar un paquete:

		pip install --upgrade nombre_del_paquete

Desinstalar un paquete:

		pip uninstall nombre_del_paquete


Eliminar el entorno:

		rmdir /s /q nombre_del_entorno 

Ver información sobre un paquete:

		pip show nombre_del_paquete




**¿QUÉ ES PIP?**

pip es el gestor de paquetes oficial de Python — es decir, una herramienta que te permite instalar, actualizar y eliminar librerías externas (también llamadas paquetes o dependencias).


**¿QUÉ ES VENV?**

*venv* (abreviatura de virtual environment) es un módulo incluido en Python que sirve para crear entornos virtuales aislados.

En palabras simples:

*venv* te permite crear una copia independiente de Python donde puedes instalar librerías sin afectar al resto del sistema ni a otros proyectos.

Piensa en ello como una “burbuja” de Python donde solo viven las dependencias de un proyecto específico.