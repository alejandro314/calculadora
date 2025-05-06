from flask import Flask, request, render_template
from operaciones import sumar, restar , multiplicar , division 

app=Flask(__name__)

@app.route("/")
def home():
    return render_template(home.html)
@app.route("/suma")
def ruta_sumar():
    num1=request.args.get("num1", type=float)
    num2=request.args.get("num2", type=float)

    if num1 is None or num2 is None:
        return "faltan datos para sumar dos datos de parametros x"


    return f"el resultado de la suma es {sumar(num1,num2)}"
@app.route("/restar")
def ruta_restar():
    num1=request.args.get("num1", type=float)
    num2=request.args.get("num2", type=float)

    if num1 is None or num2 is None:
        return "faltan datos para realizar la operacion"


    return f"el resultado de la resta es {restar(num1,num2)}"
@app.route("/multiplicar")
def ruta_multiplicar():
    num1=request.args.get("num1", type=float)
    num2=request.args.get("num2", type=float)

    if num1 is None or num2 is None:
        return "faltan datos para realizar la operacion"


    return f"el resultado de la multiplicacion  es {multiplicar(num1,num2)}"
@app.route("/division")
def ruta_division():
    num1=request.args.get("num1", type=float)
    num2=request.args.get("num2", type=float)

    if num1 is None or num2 is None:
        return "faltan datos para realizar la operacion"


    return f"el resultado de la division  es {division(num1,num2)}"

if __name__=="__main__":
    app.run(debug=True)