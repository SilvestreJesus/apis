from fastapi import FastAPI
import json
import math

app = FastAPI()

@app.get("/")
def root():
    return "API de Operaciones"

@app.get("/suma")
def suma():

    with open('.json', 'r') as file:
        data = json.load(file)    
    resultados = []
    for operacion in data:
        if operacion["tipo_operacion"] == "suma":
            resultado = operacion["valores"][0]
            for valor in operacion["valores"][1:]:
                resultado += valor
            resultados.append(f"Sumando valores: {operacion['valores']}, Resultado: {resultado}")
    return resultados


@app.get("/resta")
def resta():

    with open('.json', 'r') as file:
        data = json.load(file)    
    resultados = []
    for operacion in data:
        if operacion["tipo_operacion"] == "resta":
            resultado = operacion["valores"][0]
            for valor in operacion["valores"][1:]:
                resultado -= valor
            resultados.append(f"Restando valores: {operacion['valores']}, Resultado: {resultado}")
    return resultados


@app.get("/multiplicacion")
def multiplicacion():

    with open('.json', 'r') as file:
        data = json.load(file)    
    resultados = []
    for operacion in data:
        if operacion["tipo_operacion"] == "multiplicacion":
            resultado = operacion["valores"][0]
            for valor in operacion["valores"][1:]:
                resultado *= valor
            resultados.append(f"Multiplicando valores: {operacion['valores']}, Resultado: {resultado}")
    return resultados


@app.get("/division")
def division():

    with open('.json', 'r') as file:
        data = json.load(file)    
    resultados = []
    for operacion in data:
        if operacion["tipo_operacion"] == "division":
            resultado = operacion["valores"][0]
            for valor in operacion["valores"][1:]:
                resultado /= valor
            resultados.append(f"Dividiendo valores: {operacion['valores']}, Resultado: {resultado}")
    return resultados

@app.get("/raiz_cuadrada")
def raiz_cuadrada():

    with open('.json', 'r') as file:
        data = json.load(file)    
    resultados = []
    for operacion in data:
        if operacion["tipo_operacion"] == "raiz":
            resultadosraizes = []
            for valor in operacion["valores"]:
                resultadosraizes.append(math.sqrt(valor))
            resultados.append(f"Raiz cuadrada valores: {operacion['valores']}, Resultado: {resultadosraizes}")
    return resultados
