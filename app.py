from flask import Flask, render_template, request, redirect

app = Flask(__name__)

# Lista en memoria
habitos = []

@app.route("/")
def index():
    return render_template("dashboard.html", habitos=habitos)

@app.route("/agregar", methods=["POST"])
def agregar():
    nombre = request.form.get("nombre")
    if nombre:
        habitos.append([nombre, []])
    return redirect("/")

@app.route("/eliminar/<int:idx>")
def eliminar(idx):
    if 0 <= idx < len(habitos):
        habitos.pop(idx)
    return redirect("/")

@app.route("/marcar/<int:idx>/<string:estado>")
def marcar(idx, estado):
    if 0 <= idx < len(habitos):
        if estado == "cumplido":
            habitos[idx][1].append(1)
        elif estado == "nocumplido":
            habitos[idx][1].append(0)
    return redirect("/")

@app.route("/estadisticas")
def estadisticas():
    if not habitos:
        return render_template("estadisticas.html", estadisticas=[])

    estadisticas = []
    for nombre, progreso in habitos:
        if progreso:
            total = sum(progreso)
            porcentaje = (total / len(progreso)) * 100
            estadisticas.append([nombre, porcentaje, total, len(progreso)])
        else:
            estadisticas.append([nombre, 0, 0, 0])

    # Ordenar por porcentaje descendente
    estadisticas.sort(key=lambda x: x[1], reverse=True)

    return render_template("estadisticas.html", estadisticas=estadisticas)

if __name__ == "__main__":
    app.run(debug=True)