# Import
from flask import Flask, render_template,request, redirect
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
# Conectando SQLite
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///diary.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# Creación de una base de datos
db = SQLAlchemy(app)

# Página de contenidos en ejecución
@app.route('/')
def index():
    return render_template('index.html')
    
# CLase formulario
class Formulario(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), nullable=False)                     
    text = db.Column(db.Text, nullable=False)

# Habilidades dinámicas
@app.route('/', methods=['POST'])
def process_form():
    button_python = request.form.get('button_python')
    button_discord = request.form.get('button_discord')
    button_html = request.form.get('button_html')
    button_db = request.form.get('button_db')
    return render_template('index.html', button_python=button_python, button_discord=button_discord, button_html=button_html, button_db=button_db)
    

    if methods == 'POST':
        email = request.form.get('email')
        text = request.form.get('text')

        # Guardar en la base de datos
        new_entry = Formulario(email=email, text=text)
        db.session.add(new_entry)
        db.session.commit()

        # Redirigir a la página de inicio

        return redirect('/')
    
    return render.template('index.html',
                          button_python=button_python,
                          button_discord=button_discord,
                          button_html=button_html,
                          button_db=button_db)
                                             
if __name__ == "__main__":
    app.run(debug=True)
