from flask import Flask, render_template, request, redirect, url_for, flash, jsonify

POKEAI ="https://pokeapi.co/api/v2/pokemon/"
app = Flask(__name__)
app.secret_key = "en_el_año_sie_dos"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/search', methods="POST")
def search():
    pokemon_name = request.form.get('poke', '').strip().lower()
    if not pokemon_name:
        flash('Ingrese un pokemon', 'error')
        return redirect(url_for('index'))
    resp = request.get(f"{API}{pokemon_name}")
    
    if resp.status_code == 200:
        pokemon_data = resp.json()
        return render_template('pokemon.html', pokemon=pokemon_data)



if __name__ == "__main__":
    app.run(debug=True)