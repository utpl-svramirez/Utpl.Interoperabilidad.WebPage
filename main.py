from flask import Flask, render_template

app = Flask(__name__)

# Lista de personas
personas = [{"nombre": "Juan", "apellido": "Perez", "edad": 25},
            {"nombre": "Ana", "apellido": "Gomez", "edad": 30},
            {"nombre": "Carlos", "apellido": "Lopez", "edad": 45}]

@app.route('/')
def home():
    return render_template('index.html', personas=personas)

if __name__ == '__main__':
    app.run(debug=True)