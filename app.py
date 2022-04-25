from flask import Flask, render_template, request 

app = Flask(__name__)
frutas = []

@app.route('/', methods=["GET", "POST"])
def principal():
	# frutas= ['morango', 'uva']
	
	fruta = request.form.get('fruta')
	if request.method == 'POST':
		frutas.append(fruta)
	return render_template("index.html", frutas=frutas)

@app.route('/sobre')
def sobre():
	diario = {"joao": 6.0, "maria": 5.0, " pedro": 4.5, " lucas":6.5,"tiago": 7.5, " bruna": 8.0}
	return render_template("sobre.html", diario=diario)



app.run(debug=True)
