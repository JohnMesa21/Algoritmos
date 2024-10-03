from app.config.common import request, render_template, flash, Blueprint
from app.db.conectiondb import mysql

bp = Blueprint('register', __name__)

# @bp.route('/userregister')
# def home():
#    return render_template('index.html')

@bp.route('/userregister',  methods=["GET","POST"])
def useRegister(): 
    if request.method == "POST":
        try:
            cel = request.form['celular']  # Intentamos acceder directamente
            nom = request.form['nombre']
            ape = request.form['apellido']
            email = request.form['email']
            contrasena = request.form['password']

            # Validamos que el campo celular no esté vacío
            if not cel:
                flash('Por favor ingresa un celular', 'danger')
                return render_template('index.html')

            # Verifica que los demás campos no estén vacíos
            if not nom or not ape or not email or not contrasena:
                flash('Por favor llena todos los campos', 'danger')
                return render_template('index.html')

            # Inserción en la base de datos
            
            cur = mysql.connection.cursor()
            cur.execute("""INSERT INTO usuarios (nombre, apellido, email, celular, contrasena) 
                          VALUES (%s, %s, %s, %s, %s)""", (nom, ape, email, cel, contrasena)) 
            mysql.connection.commit()  # Asegúrate de hacer commit para guardar los cambios
            cur.close()

            flash('Usuario registrado exitosamente', 'success')
        except KeyError as e:
            flash(f'Falta el campo: {str(e)}', 'danger')
        except Exception as e:
            flash(f'Error al registrar usuario: {str(e)}', 'danger')
        finally:
            return render_template('index.html')
        
    return render_template('index.html')
