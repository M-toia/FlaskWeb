from flask import Flask, render_template, request 

app = Flask(__name__)
frutas = []
registros = []

@app.route('/', methods=["GET", "POST"])
def principal():
	# frutas= ['morango', 'uva']
	
	fruta = request.form.get('fruta')
	if request.method == 'POST':
		frutas.append(fruta)
	return render_template("index.html", frutas=frutas)

@app.route('/sobre', methods=["GET", "POST"])
def sobre():
	# diario = {"joao": 6.0, "maria": 5.0, " pedro": 4.5, " lucas":6.5,"tiago": 7.5, " bruna": 8.0}
	
    aluno = request.form.get("aluno")
    nota = request.form.get("nota")

    if request.method== 'POST':
    	registros.append({"aluno":aluno, "nota":nota})
    return render_template("sobre.html", registros=registros)


app.run(debug=True)
