from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Union
import math

app = FastAPI(title="API de Operaciones Matemáticas")


class Valores(BaseModel):
    valores: List[float]


class RespuestaOperacion(BaseModel):
    operacion: str
    valores: List[float]
    resultado: Union[float, List[float]]



@app.get("/")
def root():
    return {"API de Operaciones"}


@app.post("/suma", response_model=RespuestaOperacion)
def suma(data: Valores):
    return {
        "operacion": "suma",
        "valores": data.valores,
        "resultado": sum(data.valores)
    }


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
