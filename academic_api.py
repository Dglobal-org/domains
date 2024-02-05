from flask import Flask, request, jsonify
import re

app = Flask(__name__)


@app.route("/verify", methods=["GET"])
def verificar_dominio():
    email = request.args.get("email")

    dominio = re.findall(r"@(.*)", email)[0]

    dominios_permitidos = leer_dominios_txt("academic.txt")

    if dominio in dominios_permitidos:
        return jsonify({"Valid"})
    else:
        return jsonify({"Invalid"})

def leer_dominios_txt(archivo_txt):
    with open(archivo_txt, "r") as archivo:
        dominios = [linea.strip() for linea in archivo.readlines()]
    return dominios

if __name__ == "__main__":
    app.run()
