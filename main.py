from flask import Flask, request
from operaciones import sumar

app=Flask(__name__)

@app.route("/")
def home():
    return '''
    
    
    pagina de inicio
    Calculadora

    <a href="/suma?num1=5&num2=10"> Ir a sumar  </a>

    '''

@app.route("/suma")
def ruta_sumar():
    num1=request.args.get("num1", type=float)
    num2=request.args.get("num2", type=float)

    if num1 is None or num2 is None:
        return "faltan datos para sumar dos datos de parametros x"


    return f"el resultado de la suma es {sumar(num1,num2)}"

if __name__=="__main__":
    app.run(debug=True)