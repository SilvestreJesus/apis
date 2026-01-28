# Operaciones de Matemáticas <em style="font-size: 20px;">de  Silvestre Jesús Guadalupe Gutiérrez</em>

## Descripción del ejercicio

Este proyecto consiste en una **API REST** desarrollada con **FastAPI en Python**, que permite realizar **operaciones matemáticas** básicas a partir de una lista de números enviada por el usuario en formato JSON.

La API funciona como una **interfaz entre el usuario y la lógica matemática**, procesando los datos recibidos y devolviendo siempre una respuesta estructurada con:

**El nombre de la operación**
**Los valores enviados**
**El resultado del cálculo**

El proyecto incluye además un contenedor **Docker**, lo que permite ejecutar la aplicación sin necesidad de configurar manualmente el entorno de Python.


---
### Requisitos previos

Asegúrate de tener instalados los siguientes requisitos en tu sistema para poder ejecutar el proyecto:
* **Docker** y **Docker Compose** 
* **Python** 


## Importaciones y Librerías

* **FastAPI** : Es el framework principal. Se encarga de crear las rutas (endpoints) y gestionar las peticiones web.
* **HTTPException** : Es una herramienta de seguridad. Si algo sale mal (como dividir entre cero), permite enviarle un mensaje de error claro al usuario.

* **BaseModel (Pydantic)** : Es el "validador". Se asegura de que si pides un número, el usuario no envíe una letra. Si los datos no coinciden con el modelo, FastAPI los rechaza automáticamente.

* **typing (List, Union)** : Define que el resultado puede ser un solo número o una lista de números (como en el caso de las raíces).

* **math** : Proporciona funciones matemáticas avanzadas (como sqrt para la raíz cuadrada).


### Estructura de datos

## Titulo del programa
app = FastAPI(title="API de Operaciones Matemáticas")

## Modelo de entrada

Obliga a que el cuerpo de la petición sea un JSON con una clave llamada valores, que contiene una lista de números decimales:

``` bash
    class Valores(BaseModel):
        valores: List[float] 
```

## Modelo de salida

Todas las respuestas de la API siguen la misma estructura:

``` bash
    class RespuestaOperacion(BaseModel):
    operacion: str
    valores: List[float]
    resultado: Union[float, List[float]] 
```

## Ruta raíz
Devuelve un mensaje indicando que la API está activa.
``` bash
@app.get("/")

def root():
    return {"API de Operaciones"}
``` 

## Api Suma
Suma todos los valores enviados en la lista.
``` bash
@app.post("/suma", response_model=RespuestaOperacion)
def suma(data: Valores):
    return {
        "operacion": "suma",
        "valores": data.valores,
        "resultado": sum(data.valores)
    }
```

## Api Resta
Resta los valores de la lista en orden, empezando por el primero.
``` bash
@app.post("/resta", response_model=RespuestaOperacion)
def resta(data: Valores):
    resultado = data.valores[0]
    for v in data.valores[1:]:
        resultado -= v
    return {
        "operacion": "resta",
        "valores": data.valores,
        "resultado": resultado
    }
```

## Api Multiplicación
Multiplica todos los valores enviados.
``` bash
@app.post("/multiplicacion", response_model=RespuestaOperacion)
def multiplicacion(data: Valores):
    resultado = 1
    for v in data.valores:
        resultado *= v
    return {
        "operacion": "multiplicacion",
        "valores": data.valores,
        "resultado": resultado
    }
```
## Api División
Divide los valores en orden.
Si algún valor es 0, la API devuelve un error.
``` bash
@app.post("/division", response_model=RespuestaOperacion)
def division(data: Valores):
    resultado = data.valores[0]
    for v in data.valores[1:]:
        if v == 0:
            raise HTTPException(status_code=400, detail="No se puede dividir entre cero")
        resultado /= v
    return {
        "operacion": "division",
        "valores": data.valores,
        "resultado": resultado
    }
```
## Api Raíz cuadrada
Calcula la raíz cuadrada de cada valor.
No se permiten números negativos.
``` bash
@app.post("/raiz", response_model=RespuestaOperacion)
def raiz_cuadrada(data: Valores):
    resultados = []
    for v in data.valores:
        if v < 0:
            raise HTTPException(status_code=400, detail="No se puede sacar raíz de números negativos")
        resultados.append(math.sqrt(v))

    return {
        "operacion": "raiz cuadrada",
        "valores": data.valores,
        "resultado": resultados
    }
```

# Ejecución con Docker

## Construir la imagen
``` bash
docker build -t operaciones-matematicas .
```
## Ejecutar el contenedor
``` bash
docker run -p 8000:8000 operaciones-matematicas
```

# Despliegue en Railway

Además de ejecutarse de forma local con Docker, la API fue desplegada en **Railway**, una plataforma en la nube que permite ejecutar aplicaciones dentro de contenedores **Docker** sin necesidad de configurar servidores manualmente.

## URL de la API desplegada
https://apis-production-3987.up.railway.app/docs

## Desde esta URL es posible:

**Probar todos los endpoints**
**Enviar valores en formato JSON**
**Visualizar las respuestas de la API en tiempo real**